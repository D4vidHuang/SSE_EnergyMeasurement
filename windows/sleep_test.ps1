# Windows Sleep Energy Measurement Script
$COUNT = 30  # Total iterations
$OUTPUT_FILE = "benchmark_results_sleep.csv"

# Get the full path to `energibridge.exe`
$ENERGIBRIDGE_PATH = (Get-Location).Path + "\energibridge\energibridge.exe"

# Define the sleep command
$COMMAND_SLEEP = "$ENERGIBRIDGE_PATH --summary -m 65 timeout 60"

# Create CSV file with headers
"Iteration,Browser,Energy (Joules)" | Out-File -FilePath $OUTPUT_FILE -Encoding UTF8

Write-Host "Starting warm-up iterations..."
for ($i=0; $i -lt 5; $i++) {
    Write-Host "Running warm-up iteration $($i+1)/5..."
    Invoke-Expression $COMMAND_SLEEP | Out-Null  # Run sleep command but discard output
    Start-Sleep -Seconds 5  # Shorter pause for warm-up
}

Write-Host "Starting main test iterations..."
for ($i=0; $i -lt $COUNT; $i++) {
    Write-Host "Running command iteration $($i+1)/$COUNT..."

    # Run the command and capture output
    $OUTPUT = Invoke-Expression $COMMAND_SLEEP 2>&1
    $BROWSER = "Sleep"

    # Extract energy consumption in joules
    $ENERGY = ($OUTPUT | Select-String "Energy consumption in joules:").Line -replace ".*Energy consumption in joules: (\S+).*", '$1'

    # Handle missing energy data
    if ($ENERGY -match "^\d+(\.\d+)?$") {
        "$($i+1),$BROWSER,$ENERGY" | Out-File -FilePath $OUTPUT_FILE -Append -Encoding UTF8
        Write-Host "Energy Consumption (Joules): $ENERGY"
    } else {
        "$($i+1),$BROWSER,N/A" | Out-File -FilePath $OUTPUT_FILE -Append -Encoding UTF8
        Write-Host "Energy consumption not found in output for $BROWSER."
        Write-Host "Full Output:"
        Write-Host "$OUTPUT"
    }

    # Pause for 60 seconds between tests
    Start-Sleep -Seconds 10
}

Write-Host "All iterations completed. Results saved to $OUTPUT_FILE"
