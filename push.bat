@echo off
echo === GitHub�� �ڵ� Ǫ�� ===

REM ����ڷκ��� Ŀ�� �޽����� �Է¹���
set /p msg="Ŀ�� �޽����� �Է��ϼ���: "

git add .
git commit -m "%msg%"
git push origin main

echo.
echo === Ǫ�� �Ϸ�! ===
pause
