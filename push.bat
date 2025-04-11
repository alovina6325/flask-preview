@echo off
echo === GitHub에 코드 푸시 ===

REM 사용자로부터 커밋 메시지를 입력받음
set /p msg="커밋 메시지를 입력하세요: "

git add .
git commit -m "%msg%"
git push origin main

echo.
echo === 푸시 완료! ===
pause
