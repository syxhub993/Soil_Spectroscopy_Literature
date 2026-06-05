$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

Write-Host "Current PowerShell session is using UTF-8."
Write-Host "Try: Get-Content README.md -Encoding UTF8"
Write-Host "If this script is blocked, run: scripts\open_utf8_powershell.cmd"
