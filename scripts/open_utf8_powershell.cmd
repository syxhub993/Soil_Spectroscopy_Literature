@echo off
chcp 65001 >nul
powershell.exe -NoExit -ExecutionPolicy Bypass -Command "$OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Set-Location -LiteralPath '%~dp0..'; Write-Host 'UTF-8 PowerShell ready.'; Write-Host 'Try: Get-Content README.md -Encoding UTF8'"
