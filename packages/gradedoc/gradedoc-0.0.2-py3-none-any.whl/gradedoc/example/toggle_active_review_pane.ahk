; CTRL+ALT+W to toggle the review pane of the current document
^!w:: Run pwsh -NoExit -Command gradedoc pane; if ($LASTEXITCODE -eq 0) { exit }
