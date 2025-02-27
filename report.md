---
author: Anyan Huang, Yongcheng Huang, Yiming Chen, Philippe Henry,
title: "The browser energy efficiency revolution"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  This study investigates the energy consumption of two popular web browsers, Google Chrome and Mozilla Firefox, under realistic user scenarios on macOS, Linux and Windows. By modeling activities such as Reddit browsing and YouTube video playback, and applying baseline-corrected measurements, we provide an empirical comparison of browser efficiency. Our findings reveal that Chrome demonstrates significantly lower energy usage than Firefox for Reddit browsing , suggesting a potential avenue for substantial power savings. In contrast, no statistically significant difference emerges for YouTube playback , indicating that both browsers perform similarly in streaming scenarios. These results highlight the importance of task-specific testing and underscore how browser choice can meaningfully impact environmental footprints, particularly in energy-intensive usage patterns.
---

+ **Add your name here**
+ **Change the summary**
+ **Contrive a new title of the blog**
+ **Find a good cover(generate one using diffusion by giving the summary?)**

# Group 4 - The browser energy efficiency revolution: An empirical study of energy consumption from the perspective of user behavior


## Table of Contents


# Introduction


When 3.7 billion browser users scroll through social media feeds, hidden energy consumption differences quietly alter the digital world's carbon footprint. This study, through an automated testing framework, achieves the following for the first time:

1. **Modeling Real User Behavior** (YouTube watching, Reddit browsing)
2. **Cross-Browser Energy Benchmarking** (Firefox 121 vs. Chrome 122)
3. **System-Level Energy Isolation Measurement Techniques** (MacOS15.3.1, Fedora, Windows11)
4. **Statistical Significance Validation**

## Research Questions

- Is there a statistically significant difference in energy efficiency between different browsers in typical user scenarios? 
- How do user behavior patterns amplify the energy impact of browser choice?
- Does the energy-saving benefit of browser/operating system migration strategies have scalable application value?

## Key Findings:

**TODO: Change this to the actual data**

Our experiments reveal that, in typical usage scenarios, **Chrome consumes xxxx less energy on average compared to Firefox**, leading to an annual CO₂ reduction of **xxxx per user**. 

If **xxxx of global Firefox users switched to Chrome**, the estimated annual energy savings would reach **xxxx million kWh**—enough to power **xxx households for an entire year**.



-------------------------------------------------------------------------------------------------------------------------------------------------------

# Assessing Real-World Impact

To make our findings more relevant, we will investigate user statistics to understand the number of Firefox users across different operating systems. By calculating potential energy savings based on the average energy consumption difference between the two browsers, we can provide actionable insights for users and organizations alike.

In our testing, we will focus on several software applications that are commonly used by individuals and organizations. The primary tools under test will include:

+ **Google Chrome**: A widely used web browser known for its speed and extensive feature set.

+ **Mozilla Firefox** : An open-source browser that emphasizes privacy and customization.

We will utilize the **Energibridge** tool for measuring energy consumption during our tests. This tool allows us to capture detailed energy usage data while running various browser tasks. By employing this software, we can ensure that our measurements are accurate and reflective of real-world usage scenarios.





# User-Centric Test Scenarios

To ensure our tests accurately represent real-world browser usage, we design **user-centric scenarios** that capture typical activities. This approach provides practical insights into energy consumption beyond purely technical measurements.

## Test Protocol

- **Baseline Task:** 60-second idle period. [Implementation here](https://github.com/D4vidHuang/SSE_EnergyMeasurement/blob/linux_test/linux_scripts/auto_sleep_script.sh)
- **Iterations:** 30 runs, **2 minutes per iteration** (60 seconds active, 60 seconds idle). [Implementation here](https://github.com/D4vidHuang/SSE_EnergyMeasurement/blob/linux_test/linux_scripts/auto_script.sh)  
- **Test Cases:**
  1. **Video Streaming (YouTube):** Measure energy usage during continuous video playback.  

    ```Python
    def play_youtube_video(duration_seconds=60):
        driver = webdriver.Firefox()  # Ensure geckodriver is in PATH

        try:
            driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            wait = WebDriverWait(driver, 5)
            try:
                accept_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Accept all')]]")))
                accept_all_button.click()
                time.sleep(5)
            except TimeoutException:
                print("Accept all not found")
            try:
                play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-large-play-button')]")))
                play_button.click()
                print("Clicked Play button.")
            except:
                print("Play button not found or already playing.")
            time.sleep(duration_seconds)
        
        finally:
            driver.quit()
    ```

  2. **Social Media Browsing (Reddit):** Assess energy consumption while scrolling and interacting with content.  

    ```python
      def browse_reddit(duration_seconds=60):
      driver = webdriver.Firefox()  # geckodriver is assumed to be in PATH

      try:
          driver.get("https://www.reddit.com")

          time.sleep(5)  # Initial wait

          start_time = time.time()
          while time.time() - start_time < duration_seconds:
              driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
              time.sleep(2)  # Wait briefly between scrolls

      finally:
          driver.quit()
    ```

## Testing Configuration

### Software Versions

| Component        | Version       |
|-----------------|--------------|
| Google Chrome   | 133.0.6943.99 |
| Mozilla Firefox | 135.0         |
| Energibridge    | v0.0.7        |

### Test Environment

#### Linux
Machine: ASUS Zenbook 14 UX3405MA

  + Processor: Intel® Core™ Ultra 9 185H × 22
  + Memory: 32.0 GiB

Operating System: Fedora Linux 41 (Workstation Edition)

  + Kernel Version: Linux 6.12.15-200.fc41.x86_64
  + Windowing System: Wayland

#### MacOS

**Note:** _TODO: Specify System completely_

#### Windows  
**Machine:** Personal PC  
  - **Processor:** Intel® Core™ i9-12900K  
  - **Memory:** 32.0 GiB  

**Operating System:** Windows 11 Professional  
  - **Version:** 23H2 (Build 22631.4890)  

 

### Experimental Controls

#### **Zen Mode (Minimized System Interference)**  
To ensure consistency, we reduce system background activity as follows:  

- Close all non-essential applications.  
- Disable notifications.  
- Disconnect unnecessary peripherals (USB drives, external displays, etc.).  
- Stop background services (e.g., web servers, file-sharing tools).  
- Disable network connectivity if not required.  
- Prefer wired connections over wireless for stability.  

#### **Configuration Freezing (Eliminating Variability)**  
To maintain test consistency, we **fix and document** key settings:  

- **Display Configuration:** Lock brightness and resolution to a fixed value.  
- **Power Management:** Disable automatic brightness adjustment and dynamic power-saving features.  
- **Network Conditions:** Ensure stable network settings to prevent fluctuations in energy usage.  

By enforcing strict experimental controls, we **minimize variability** and ensure the reproducibility of our results.


# Statistical Significance Testing Formulas

## T-Statistic
The T-Statistic measures the significance of the difference between the means of two samples. It is calculated as:

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

where:
- $\bar{X}_1$, $\bar{X}_2$ are the means of the two samples,
- $s_1^2$, $s_2^2$ are the variances of the two samples,
- $n_1$, $n_2$ are the sizes of the two samples.

---

## P-Value
The P-Value represents the probability of observing the current or a more extreme test statistic under the null hypothesis. For a two-sample t-test, it is given by:

$$
p = 2 \cdot \text{CDF}_t(-|t|; \text{df})
$$

where:
- $\text{CDF}_t$ is the cumulative distribution function of the t-distribution,
- $|t|$ is the absolute value of the t-statistic,
- $\text{df}$ is the degrees of freedom, calculated as:

$$
\text{df} = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1-1} + \frac{(s_2^2/n_2)^2}{n_2-1}}
$$

---

### Significance Criterion
- If $p < \alpha$ (typically $\alpha = 0.05$), reject the null hypothesis, indicating a significant difference between the two sample means.
- If $p \geq \alpha$, there is insufficient evidence to reject the null hypothesis.


# Testing Results


## MacOS

This section summarizes the **macOS** test outcomes for **Chrome** and **Firefox** under two common usage scenarios: **Reddit browsing** and **YouTube video playback**. All values have been baseline-corrected using an average sleep energy measurement of **240.68 Joules**, following outlier removal.

- **Figure 1**: ![Average Power Consumption by Browser (Reddit Task)](/img/AvgPowerConsumptionRedditMacOS.png)  
- **Figure 2**: ![Average Power Consumption by Browser (YouTube Task)](/img/AvgPowerConsumptionYoutubeMacOS.png)  
- **Figure 3**: ![Reddit Browsing – Adjusted Energy Consumption by Browser](img/AvgRedditMacOS.png)
- **Figure 4**: ![YouTube Playback – Adjusted Energy Consumption by Browser](img/AvgPowerYoutubeMacOS.png)

---

### Chrome

#### Reddit Browsing Task
- **Baseline Average Energy (post-outlier removal):** 240.68 Joules  
- **Data Cleaning:** One negative outlier (Iteration 59: –0.065 Joules) was excluded.  
- **Statistical Analysis:**  
  - **t-statistic:** 12.43  
  - **p-value:** 7.20e-18  

**Interpretation:** As shown in Figures 1 and 3, Chrome demonstrates a statistically significant lower energy consumption for Reddit browsing compared to Firefox. The **p-value (7.20e-18)** strongly suggests that the observed difference is unlikely due to random chance.

#### YouTube Playback Task
- **Baseline Average Energy (post-outlier removal):** 240.68 Joules  
- **Data Cleaning:** No negative outliers were detected.  
- **Statistical Analysis:**  
  - **t-statistic:** 1.26  
  - **p-value:** 0.211  

**Interpretation:** In Figures 2 and 4, the YouTube playback energy usage for Chrome and Firefox appears more similar. The **p-value (0.211)** indicates that the difference in average energy consumption between the two browsers is **not** statistically significant in this scenario.

---

### Firefox

#### Reddit Browsing Task
- **Outcome:** Firefox generally shows higher adjusted energy usage than Chrome.  
- **Statistical Outcome:** With a **p-value of 7.20e-18**, the difference in energy consumption between Firefox and Chrome for Reddit browsing is highly significant.

**Interpretation:** Figures 1 and 3 reveal that Firefox’s energy consumption is noticeably greater than Chrome’s for the Reddit task, supporting the t-test result that confirms a meaningful difference.

#### YouTube Playback Task
- **Outcome:** Firefox’s energy consumption for YouTube playback is broadly on par with Chrome’s.  
- **Statistical Outcome:** With a **p-value of 0.211**, there is no statistically significant difference between Firefox and Chrome.

**Interpretation:** Figures 2 and 4 show overlapping energy distributions for both browsers. The data do not provide sufficient evidence to conclude one browser is more efficient than the other in YouTube playback.

---

## Windows

This section summarizes the **Windows** test outcomes for **Chrome** and **Firefox** under two common usage scenarios: **Reddit browsing** and **YouTube video playback**. All values have been baseline-corrected using an average sleep energy measurement of **455.0382 Joules**, following outlier removal.

- **Figure 1**: ![Average Power Consumption by Browser (Reddit Task)](img/win-reddit.jpg)  
- **Figure 2**: ![Average Power Consumption by Browser (YouTube Task)](img/win-youtube.jpg)  

---

### Reddit Browsing Task
- **Figure 3**: ![Reddit Browsing – Adjusted Energy Consumption by Browser](img/win-vio-reddit.jpg)  
- **Baseline Average Energy (post-outlier removal):** 455.0382 Joules  
- **Data Cleaning:** No negative outliers were detected.  
- **Statistical Analysis:**  
  - **t-statistic:** 19.22  
  - **p-value:** 7.80e-27  

**Interpretation:** As shown in Figures 1 and 3, Chrome demonstrates a statistically significant lower energy consumption for Reddit browsing compared to Firefox. The **p-value (7.80e-27)** confirms that this difference is highly significant and unlikely due to random chance.

From a sustainability perspective, this means that **using Chrome for Reddit browsing could result in measurable energy savings**, reducing power consumption and contributing to a lower environmental footprint. Over time, this could lead to more efficient resource use and lower electricity costs for users.

---

### YouTube Playback Task
- **Figure 4**: ![YouTube Playback – Adjusted Energy Consumption by Browser](img/win-vio-youtube.jpg)  
- **Baseline Average Energy (post-outlier removal):** 455.0382 Joules  
- **Data Cleaning:** No negative outliers were detected.  
- **Statistical Analysis:**  
  - **t-statistic:** -1.88  
  - **p-value:** 0.0652  

**Interpretation:** In Figures 2 and 4, the YouTube playback energy usage for Chrome and Firefox appears more similar. The **p-value (0.0652)** suggests that the difference in average energy consumption is **not statistically significant** at the 0.05 threshold, although it is marginally close.

This indicates that for **YouTube playback, both browsers perform similarly in terms of energy consumption**, meaning there is no clear advantage in choosing one over the other purely for energy efficiency purposes.

---
## Linux
This section summarizes the **Linux** test outcomes for **Chrome** and **Firefox** under two common usage scenarios: **Reddit browsing** and **YouTube video playback**. All values have been baseline-corrected using an average sleep energy measurement of **502.46 Joules**, following outlier removal.

- **Figure 5**: ![Average Power Consumption by Browser (Reddit Task)](/img/reddit_power_hist_linux.png)  
- **Figure 6**: ![Average Power Consumption by Browser (YouTube Task)](/img/yt_power_hist_linux.png)  
- **Figure 7**: ![Reddit Browsing – Adjusted Energy Consumption by Browser](/img/reddit_power_violin_linux.png)
- **Figure 8**: ![YouTube Playback – Adjusted Energy Consumption by Browser](/img/yt_power_violing_linux.png)

---

### Reddit Browsing Task
- **Baseline Average Energy (post-outlier removal):** 502.46 Joules  
- **Data Cleaning:** No negative outliers were detected.  
- **Statistical Analysis:**  
  - **t-statistic:** 10.77  
  - **p-value:** 1.81e-15  

**Interpretation:** As shown in Figures 5 and 7, Chrome demonstrates a statistically significant lower energy consumption for Reddit browsing compared to Firefox. The **p-value (1.81e-15)** strongly suggests that the observed difference is unlikely due to random chance.

### YouTube Playback Task
- **Baseline Average Energy (post-outlier removal):** 502.46 Joules  
- **Data Cleaning:** No negative outliers were detected.  
- **Statistical Analysis:**  
  - **t-statistic:** -0.96  
  - **p-value:** 0.336  

**Interpretation:** In Figures 6 and 8, the YouTube playback energy usage for Chrome and Firefox appears more similar. The **p-value (0.336)** indicates that the difference in average energy consumption between the two browsers is **not** statistically significant in this scenario.

---

## Results Table
### Reddit Scrolling

|          | Linux         | Windows         | MacOS                      |
|----------|:-------------:|:---------------:|:---------------------------:|
| **Firefox**  | avgLinuxFirefox | Text is centered | And this is right-aligned  |
| **Chrome**   | avgLinux Chrome    | Even more text   | And even more to the right |

### Youtube Streaming

|          | Linux         | Windows         | MacOS                      |
|----------|:-------------:|:---------------:|:---------------------------:|
| **Firefox**  | avgLinuxFirefox | Text is centered | And this is right-aligned  |
| **Chrome**   | avgLinux Chrome    | Even more text   | And even more to the right |

# Conclusion

By focusing on user-centric scenarios and emphasizing the real-world impact of our findings, this project aims to provide valuable insights into the energy consumption of web browsers. Through our testing, we hope to encourage users to make informed decisions that contribute to a more sustainable digital environment.

