git add .
git status
set /p Input=Commit Message:
git commit -m "%Input%"
git pull origin main
git push origin main