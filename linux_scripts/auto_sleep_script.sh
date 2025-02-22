#!/bin/bash

# Number of times to run each command sequence
COUNT=30

# Define command sequences correctly
COMMAND_SLEEP="sudo ./energibridge --summary -m 65 -- sudo -u phildo sleep 60"
# Create an array with 30 of each sequence, then shuffle


# Output CSV file
# OUTPUT_FILE="benchmark_results_balls.csv"
OUTPUT_FILE="benchmark_results_sleep.csv"

# Create CSV header
echo "Iteration,Browser,Energy (Joules)" > "$OUTPUT_FILE"

echo "Starting warm-up iterations..."
for ((i=0; i<5; i++)); do
    echo "Running warm-up iteration $((i+1)) of 5..."
    eval "$COMMAND_SLEEP" > /dev/null 2>&1
    sleep 60
done


# Loop to run the command 60 times in shuffled order
for ((i=0; i<COUNT; i++)); do
    echo "Running command iteration $((i+1)) of $COUNT..."

    BROWSER="Sleep"
    OUTPUT=$(eval "$COMMAND_SLEEP" 2>&1) # Capture both stdout and stderr

    # Extract energy consumption
    #Energy consumption in joules: 26.10137939453125 for 5.2023396 sec of execution.
    ENERGY=$(echo "$OUTPUT" | grep "Energy consumption in joules:" | awk '{print $5}')
    TIME=

    # Check if energy value was found and write to CSV
    if [[ -n "$ENERGY" ]]; then
        echo "$((i+1)),$BROWSER,$ENERGY" >> "$OUTPUT_FILE"
        echo "Energy Consumption (Joules): $ENERGY" # Optional: print to console
    else
        echo "$((i+1)),$BROWSER," >> "$OUTPUT_FILE" # Write empty energy value
        echo "Energy consumption not found in output for $BROWSER. Full Output:"
        echo "$OUTPUT" # Print the full output for debugging
    fi

    sleep 60  # Wait before the next iteration
done

echo "All iterations completed. Results saved to $OUTPUT_FILE"