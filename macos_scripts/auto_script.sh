#!/bin/bash

# Number of times to run each command sequence
COUNT=60

# Define command sequences correctly
# COMMAND_FIREFOX="sudo ./energibridge --summary -m 63 -- sudo -u phildo firefox https://dacris.github.io/jsmark/WebGLDemo.html"
# COMMAND_CHROME="sudo ./energibridge --summary -m 63 -- sudo -u phildo google-chrome https://dacris.github.io/jsmark/WebGLDemo.html"

COMMAND_FIREFOX="./energibridge --summary -m 60 python firefox_interaction.py"
COMMAND_CHROME="./energibridge --summary -m 60 python chrome_interaction.py"

# Create an array with 30 of each sequence, then shuffle
SEQUENCE_LIST=($(for i in {1..30}; do echo 0; echo 1; done | awk 'BEGIN{srand();}{print rand(), $0}' | sort -n | cut -d ' ' -f2))

# Output CSV file
OUTPUT_FILE="benchmark_results_reddit.csv"

# Create CSV header
echo "Iteration,Browser,Energy (Joules), Time (Seconds)" > "$OUTPUT_FILE"

echo "Starting warm-up iterations..."
for ((i=0; i<5; i++)); do
    echo "Running warm-up iteration $((i+1)) of 5..."
    # eval "$COMMAND_FIREFOX" > /dev/null 2>&1
    eval "$COMMAND_CHROME" > /dev/null 2>&1
    sleep 60
done

# Main benchmark loop
for ((i=0; i<COUNT; i++)); do
    BROWSER_INDEX=${SEQUENCE_LIST[$i]}

    if [ "$BROWSER_INDEX" -eq 0 ]; then
        BROWSER="Firefox"
        COMMAND="$COMMAND_FIREFOX"
    else
        BROWSER="Chrome"
        COMMAND="$COMMAND_CHROME"
    fi

    echo "Running $BROWSER (Iteration $((i+1))/$COUNT)..."
    
    # Execute command and capture output
    OUTPUT=$($COMMAND 2>&1)
    EXIT_CODE=$?

    # Parse energy and time
    ENERGY=$(echo "$OUTPUT" | awk '/Energy consumption in joules:/ {print $5}')
    TIME=$(echo "$OUTPUT" | awk '/Energy consumption in joules:/ {print $9}')

    # Handle failures
    if [ $EXIT_CODE -ne 0 ] || [[ -z "$ENERGY" || -z "$TIME" ]]; then
        echo "Warning: $BROWSER failed or missing data (Iteration $((i+1)))" >&2
        ENERGY="N/A"
        TIME="N/A"
    fi

    # Save result to CSV
    echo "$((i+1)),$BROWSER,$ENERGY,$TIME" >> "$OUTPUT_FILE"

    echo "Energy: $ENERGY Joules, Time: $TIME sec"
    sleep 60
done

echo "All iterations completed. Results saved to $OUTPUT_FILE"