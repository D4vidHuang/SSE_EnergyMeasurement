import platform
import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

energibridge_executable = "release-energibridge/energibridge"

def run_once(file_name):
    current_os = platform.system().lower()
    if current_os == 'darwin':
        current_directory = os.getcwd()
        script_path = os.path.join(current_directory, file_name)
        subprocess.run(['chmod', '+x', script_path])
        result = subprocess.run(
            [
                energibridge_executable,
                '-o', 'temp.csv',
                '--summary',
                'python3',
                script_path
            ],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print(result.stderr)

        if result.returncode == 0:
            print("Command executed successfully.")
            try:
                df = pd.read_csv('temp.csv')
                print("Data loaded successfully.")
                return df
            except Exception as e:
                print("Error loading data:", e)
                return None
        else:
            print("Error executing command.")
            return None
    else:
        raise NotImplementedError(f"Unsupported operating system: {current_os}")


# warmup
def run_test(file_name, warmup_runs=5, test_runs=60):
    print(f"Starting warm-up, total {warmup_runs} run(s).")
    for i in range(warmup_runs):
        _ = run_once(file_name)
    print(f"Starting actual test, total {test_runs} run(s).")
    all_data = []
    for i in range(test_runs):
        print(f"Run {i+1}/{test_runs}")
        df = run_once(file_name)
        if df is not None:
            all_data.append(df)

    return all_data


def extract_time_and_power(df, cumulative=False):
    time_col_index = 0
    power_col_index = 32

    data_np = df.to_numpy()
    time = data_np[:, time_col_index]
    power = data_np[:, power_col_index]
    if not cumulative:
        power = np.diff(power)
        power = np.insert(power, 0, 0)

    if cumulative:
        time = np.cumsum(time) / 1000
        power = np.cumsum(power)

    else:
        pass

    return np.column_stack((time, power))


def make_time_series_plot(time_power_dataset, cumulative=False):

    for idx, time_power in enumerate(time_power_dataset):
        time = time_power[:, 0]
        power = time_power[:, 1]

        if not cumulative:

            energy = power * (time / 1000.0)
            time = np.cumsum(time) / 1000.0
            plt.plot(time, energy, label=f'Run {idx+1}')
        else:
            plt.plot(time, power, label=f'Run {idx+1}')

    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)' if cumulative else 'Energy (J)')
    plt.title(f'{"Cumulative" if cumulative else "Non-cumulative"} Time Series')
    plt.show()


def make_violin_plot(time_power_dataset, std_dev=None):

    energy_data = []
    for time_power in time_power_dataset:
        time = time_power[:, 0]
        power = time_power[:, 1]
        dt = np.diff(time, prepend=0)
        energy = np.sum(power * dt)
        energy_data.append(energy)

    energy_data = np.array(energy_data)
    if std_dev is not None:
        mean_val = np.mean(energy_data)
        std_val = np.std(energy_data)
        mask = np.abs(energy_data - mean_val) <= std_dev * std_val
        energy_data = energy_data[mask]

    fig, ax = plt.subplots()

    print("Energy data:", energy_data)

    violins = ax.violinplot(
        energy_data,
        widths=0.6,
        showextrema=True,
        showmeans=True,
        showmedians=True
    )

    for pc in violins['bodies']:
        pc.set_facecolor('white')
        pc.set_edgecolor('black')
        pc.set_linewidth(0.6)
        pc.set_alpha(1)

    lineprops = dict(linewidth=0.5)
    medianprops = dict(color='red')
    ax.boxplot(
        energy_data,
        widths=0.3,
        whiskerprops=lineprops,
        boxprops=lineprops,
        medianprops=medianprops,
        positions=[1.15]
    )

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_ylabel("Energy Consumption (J)")
    plt.title("Violin Plot of Energy Consumption")
    plt.show()

    return energy_data


def compute_p_value(energy_data, baseline=0.0):

    t_stat, p_val = ttest_1samp(energy_data, baseline)
    print(f"One-sample t-test relative to baseline={baseline}:")
    print(f"  t-stat: {t_stat}")
    print(f"  p-value: {p_val}")
    return p_val


if __name__ == "__main__":

    test_script = "benchmark2_firefox.py"

    all_dfs = run_test(test_script, warmup_runs=5, test_runs=60)

    if not all_dfs:
        print("No valid data collected. Abort.")
        exit(1)

    time_power_runs = []
    for df in all_dfs:
        arr = extract_time_and_power(df, cumulative=True)
        time_power_runs.append(arr)

    make_time_series_plot(time_power_runs, cumulative=True)
    energy_data = make_violin_plot(time_power_runs, std_dev=None)

    # baseline=350 J
    p_val = compute_p_value(energy_data, baseline=350.0)
    if p_val < 0.05:
        print("Good(p < 0.05)")
    else:
        print("Bad(p >= 0.05)")
