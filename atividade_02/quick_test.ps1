#!/usr/bin/env pwsh

Write-Host "=== Quick Benchmark Test ==="
Write-Host "Testing Java, Python, and JavaScript implementations..."
Write-Host ""

# Initialize CSV
"Language,Iteration,Time(seconds)" | Out-File -FilePath "benchmark_results.csv" -Encoding UTF8

$iterations = 30

# Test Java
Write-Host "=== Java Test ==="
Set-Location Java

Write-Host "Compiling Java..."
javac *.java
if ($LASTEXITCODE -ne 0) {
    Write-Host "Java compilation failed!"
    exit 1
}

$javaTotal = 0
for ($i = 1; $i -le $iterations; $i++) {
    Write-Host "Java iteration $i..."
    $time = Measure-Command { java Main | Out-Null }
    $seconds = $time.TotalSeconds
    Write-Host "  Time: $seconds s"
    "Java,$i,$seconds" | Out-File -FilePath "..\benchmark_results.csv" -Append -Encoding UTF8
    $javaTotal += $seconds
}

Set-Location ..
$javaAvg = $javaTotal / $iterations

# Test Python
Write-Host ""
Write-Host "=== Python Test ==="
Set-Location Python

$pythonTotal = 0
for ($i = 1; $i -le $iterations; $i++) {
    Write-Host "Python iteration $i..."
    $time = Measure-Command { py main.py | Out-Null }
    $seconds = $time.TotalSeconds
    Write-Host "  Time: $seconds s"
    "Python,$i,$seconds" | Out-File -FilePath "..\benchmark_results.csv" -Append -Encoding UTF8
    $pythonTotal += $seconds
}

Set-Location ..
$pythonAvg = $pythonTotal / $iterations

# Test JavaScript
Write-Host ""
Write-Host "=== JavaScript Test ==="
Set-Location JavaScript

$jsTotal = 0
for ($i = 1; $i -le $iterations; $i++) {
    Write-Host "JavaScript iteration $i..."
    $time = Measure-Command { node main.js | Out-Null }
    $seconds = $time.TotalSeconds
    Write-Host "  Time: $seconds s"
    "JavaScript,$i,$seconds" | Out-File -FilePath "..\benchmark_results.csv" -Append -Encoding UTF8
    $jsTotal += $seconds
}

Set-Location ..
$jsAvg = $jsTotal / $iterations

# Add averages
"Java,Average,$javaAvg" | Out-File -FilePath "benchmark_results.csv" -Append -Encoding UTF8
"Python,Average,$pythonAvg" | Out-File -FilePath "benchmark_results.csv" -Append -Encoding UTF8
"JavaScript,Average,$jsAvg" | Out-File -FilePath "benchmark_results.csv" -Append -Encoding UTF8

Write-Host ""
Write-Host "=== Results ==="
Write-Host "Java average: $javaAvg s"
Write-Host "Python average: $pythonAvg s"
Write-Host "JavaScript average: $jsAvg s"

Write-Host ""
Write-Host "Results saved to benchmark_results.csv"

Write-Host ""
Write-Host "Generating Excel report..."
py generate_excel.py

Write-Host ""
Write-Host "Benchmark completed!"