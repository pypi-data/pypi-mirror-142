copier -f -r b2ba580
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv --upgrade-deps
. tooling/update.ps1
