# Windows 版基准测试脚本
$COUNT = 60  # 正式测试轮数
$OUTPUT_FILE = "benchmark_results_windows.csv"

# 获取 energibridge.exe 的完整路径
$ENERGIBRIDGE_PATH = (Get-Location).Path + "\energibridge\energibridge.exe"

# 恢复 `$COMMAND_FIREFOX` 和 `$COMMAND_CHROME` 为字符串格式
$COMMAND_FIREFOX = "$ENERGIBRIDGE_PATH --summary -m 60 python .\benchmarks\test_firefox.py"
$COMMAND_CHROME = "$ENERGIBRIDGE_PATH --summary -m 60 python .\benchmarks\test_chrome.py"

# 生成随机顺序（30次Firefox, 30次Chrome）
$SEQUENCE_LIST = @(0)*30 + @(1)*30 | Get-Random -Count 60
$stdoutFile = "temp_stdout.log"

# 创建 CSV 文件
"Iteration,Browser,Energy (Joules),Time (Seconds)" | Out-File -FilePath $OUTPUT_FILE -Encoding UTF8

Write-Host "Starting benchmark iterations..."

for ($i=0; $i -lt $COUNT; $i++) {
    $BROWSER_INDEX = $SEQUENCE_LIST[$i]
    
    if ($BROWSER_INDEX -eq 0) {
        $BROWSER = "Firefox"
        $COMMAND = $COMMAND_FIREFOX
    } else {
        $BROWSER = "Chrome"
        $COMMAND = $COMMAND_CHROME
    }

    Write-Host "Running $BROWSER (Iteration $($i+1)/$COUNT)..."


    # **🔹 启动进程, 仅重定向标准输出**
    $Process = Start-Process -FilePath "powershell.exe" `
        -ArgumentList "-ExecutionPolicy Bypass -Command `"$COMMAND`"" `
        -NoNewWindow -PassThru `
        -RedirectStandardOutput $stdoutFile

    # **🔹 等待最多 65 秒**
    $Process | Wait-Process -Timeout 65 -ErrorAction SilentlyContinue

    # **🔹 如果进程仍在运行，强制终止**
    if ($Process -and !$Process.HasExited) {
        Write-Host "$BROWSER test stuck! Killing process..."
        Stop-Process -Id $Process.Id -Force
    }

    Write-Host "Wait IO"
    Start-Sleep -Seconds 5

    $OUTPUT = if (Test-Path $stdoutFile) { 
        $RAW_OUTPUT = Get-Content $stdoutFile -Raw
        $RAW_OUTPUT = $RAW_OUTPUT.TrimEnd()  # 仅去除末尾的空白字符
        $RAW_OUTPUT -split "`r?`n" | Select-Object -Last 1  # 只取最后一行
    } else { "" }

    # $EXIT_CODE = $LASTEXITCODE

    # **🔹 解析能耗和时间**
    $ENERGY = ($OUTPUT | Select-String "Energy consumption in joules:").Line -replace ".*Energy consumption in joules: (\S+).*", '$1'
    $TIME = ($OUTPUT | Select-String "Energy consumption in joules:").Line -replace ".*for (\S+) sec.*", '$1'

    # # **🔹 处理失败情况**
    # if ($EXIT_CODE -ne 0 -or -not $ENERGY -or -not $TIME) {
    #     Write-Host "Warning: $BROWSER failed or missing data (Iteration $($i+1))" -ForegroundColor Yellow
    #     $ENERGY = "N/A"
    #     $TIME = "N/A"
    # }

    # **🔹 记录结果到 CSV**
    "$($i+1),$BROWSER,$ENERGY,$TIME" | Out-File -FilePath $OUTPUT_FILE -Append -Encoding UTF8

    Write-Host "Energy: $ENERGY Joules, Time: $TIME sec"

    # **🔹 休息 15 秒**
    Start-Sleep -Seconds 15
}

Write-Host "All iterations completed. Results saved to $OUTPUT_FILE"
