import subprocess

# Launch PowerShell window with the specified title and commands
subprocess.Popen([
    'powershell.exe',
    '-NoExit',  # Keeps the window open after execution unless explicitly exited
    '-Command',
    '& { $host.UI.RawUI.WindowTitle = "VEQ2002-Docs"; '
    'Write-Host "Starting script"; '
    'cd "C:\\git-toxin06\\eqemu-docs-v2"; '
    'if ($?) { '
    '    Write-Host "Directory changed successfully"; '
    '    Start-Sleep -Seconds 1; '
    '    Write-Host "Running mkdocs build..."; '
    '    mkdocs build 2>&1 | Tee-Object -Variable result; '
    '    Write-Host "Build completed"; '
    '    if ($result | Where-Object { $_ -match "Documentation built in " }) { '
    '        Write-Host "Build successful, waiting 15 seconds..."; '
    '        Start-Sleep -Seconds 15; '
    '        exit '
    '    } else { '
    '        Write-Host "Build may have failed, press enter to close"; '
    '        Read-Host '
    '    } '
    '} else { '
    '    Write-Host "Directory not found or inaccessible."; '
    '    Read-Host "Press Enter to close" '
    '} }'
], shell=True)