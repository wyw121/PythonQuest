@echo off
chcp 65001 >nul
title PythonQuest - LeetCode学习工作区

echo.
echo 🐍 PythonQuest - LeetCode学习工作区
echo =======================================
echo.
echo 常用命令:
echo.
echo 📝 创建新题目:
echo    python tools/new_leetcode.py --number 题号 --title "题目名" --category 分类 --difficulty 难度
echo.
echo 📊 查看进度:
echo    python tools/progress.py
echo.
echo 🧪 运行测试 (在题目目录下):
echo    python solution.py
echo.
echo 📚 查看详细使用说明:
echo    type docs\usage_guide.md
echo.
echo =======================================
echo 当前目录: %CD%
echo Python环境: C:\Users\wywyw\AppData\Local\Programs\Python\Python312\python.exe
echo =======================================
echo.

cmd /k
