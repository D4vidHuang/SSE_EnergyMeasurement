#!/bin/bash

# Number of times to run each command sequence
COUNT=60

# Define command sequences correctly
# COMMAND_FIREFOX="sudo ./energibridge --summary -m 60 -- sudo -u phildo firefox https://dacris.github.io/jsmark/WebGLDemo.html"
# COMMAND_CHROME="sudo ./energibridge --summary -m 60 -- sudo -u phildo google-chrome https://dacris.github.io/jsmark/WebGLDemo.html"

COMMAND_FIREFOX="sudo ./energibridge --summary -m 60 -- sudo -u phildo python3 firefox_interaction.py"
COMMAND_CHROME="sudo ./energibridge --summary -m 60 -- sudo -u phildo python3 chrome_interaction.py"

# Create an array with 30 of each sequence, then shuffle
SEQUENCE_LIST=($(seq 0 1 | xargs -I {} bash -c 'for i in {1..30}; do echo {}; done' | shuf))

# Output CSV file
OUTPUT_FILE="benchmark_results_youtube.csv"

# Create CSV header
echo "Iteration,Browser,Energy (Joules), Time (Seconds)" > "$OUTPUT_FILE"

echo "Starting warm-up iterations..."
for ((i=0; i<5; i++)); do
    echo "Running warm-up iteration $((i+1)) of 5..."
    eval "$COMMAND_FIREFOX" > /dev/null 2>&1
    # eval "$COMMAND_CHROME" > /dev/null 2>&1
    echo "Sleeping for 60 seconds..."
    sleep 60
done

# Loop to run the command 60 times in shuffled order
for ((i=0; i<COUNT; i++)); do
    SEQ_INDEX=${SEQUENCE_LIST[$i]}

    echo "Running command iteration $((i+1)) of $COUNT..."

    if [ "$SEQ_INDEX" -eq 0 ]; then
        echo "Running Firefox command..."
        BROWSER="Firefox"
        OUTPUT=$(eval "$COMMAND_FIREFOX" 2>&1)
        if [ $? -ne 0 ]; then
            echo "Error: Firefox command failed (iteration $((i+1))). Exiting." >&2
            exit 1
        fi
    else
        echo "Running Chrome command..."
        BROWSER="Chrome"
        OUTPUT=$(eval "$COMMAND_CHROME" 2>&1)
        if [ $? -ne 0 ]; then
            echo "Error: Chrome command failed (iteration $((i+1))). Exiting." >&2
            exit 1
        fi
    fi

    ENERGY=$(echo "$OUTPUT" | sed -n 's/Energy consumption in joules: \([0-9.]*\) for \([0-9.]*\) sec of execution./\1/p')
    TIME=$(echo "$OUTPUT" | sed -n 's/Energy consumption in joules: \([0-9.]*\) for \([0-9.]*\) sec of execution./\2/p')

    if [[ -n "$ENERGY" && -n "$TIME" ]]; then
        echo "$((i+1)),$BROWSER,$ENERGY,$TIME" >> "$OUTPUT_FILE"
        echo "Energy Consumption (Joules): $ENERGY, Execution Time (sec): $TIME"
    else
        echo "$((i+1)),$BROWSER,," >> "$OUTPUT_FILE"  # Empty values if not found
        echo "Energy and/or time not found in output for $BROWSER. Full Output (Iteration $((i+1))):" >&2
        echo "$OUTPUT" >&2  # Stderr
    fi

    sleep 60
done

echo "All iterations completed. Results saved to $OUTPUT_FILE"