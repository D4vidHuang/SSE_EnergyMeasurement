#!/bin/bash

COUNT=30
COMMAND_SLEEP="./energibridge --summary -m 65 -- sleep 60"
OUTPUT_FILE="benchmark_results_sleep.csv"

echo "Iteration,Browser,Energy (Joules)" > "$OUTPUT_FILE"

echo "Starting warm-up iterations..."
for ((i=0; i<5; i++)); do
    echo "Running warm-up iteration $((i+1)) of 5..."
    eval "$COMMAND_SLEEP" > /dev/null 2>&1
    sleep 60
done

for ((i=0; i<COUNT; i++)); do
    echo "Running command iteration $((i+1)) of $COUNT..."

    BROWSER="Sleep"
    OUTPUT=$(eval "$COMMAND_SLEEP" 2>&1)

    ENERGY=$(echo "$OUTPUT" | grep "Energy consumption in joules:" | awk '{print $5}')

    if [[ -n "$ENERGY" ]]; then
        echo "$((i+1)),$BROWSER,$ENERGY" >> "$OUTPUT_FILE"
        echo "Energy Consumption (Joules): $ENERGY"
    else
        echo "$((i+1)),$BROWSER," >> "$OUTPUT_FILE"
        echo "Energy consumption not found in output for $BROWSER. Full Output:"
        echo "$OUTPUT"
    fi

    sleep 60
done

echo "All iterations completed. Results saved to $OUTPUT_FILE"