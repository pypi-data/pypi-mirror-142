copier -f -r 16fc09d
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv
. tooling/update.ps1
