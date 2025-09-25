#!/usr/bin/env python3
"""
PythonQuest 快速启动菜单

提供常用功能的交互式菜单
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PYTHON_EXE = "C:/Users/wywyw/AppData/Local/Programs/Python/Python312/python.exe"


def show_menu():
    """显示主菜单"""
    print("=" * 50)
    print("🐍 PythonQuest - LeetCode 学习工作区")
    print("=" * 50)
    print("1. 📝 创建新的LeetCode题目")
    print("2. 📊 查看学习进度")
    print("3. 🎯 打开最近的题目")
    print("4. 📚 打开使用指南")
    print("5. 🔧 运行测试")
    print("0. 🚪 退出")
    print("-" * 50)


def create_new_problem():
    """创建新题目的交互式界面"""
    print("\n📝 创建新的LeetCode题目")
    print("-" * 30)

    try:
        number = int(input("题目编号: "))
        title = input("题目名称 (英文): ")

        print("\n选择分类:")
        categories = {
            "1": "array",
            "2": "string",
            "3": "linked_list",
            "4": "tree",
            "5": "dynamic_programming",
            "6": "graph",
        }

        for key, value in categories.items():
            print(f"  {key}. {value}")

        cat_choice = input("选择分类 (1-6): ")
        category = categories.get(cat_choice, "array")

        print("\n选择难度:")
        difficulties = {"1": "easy", "2": "medium", "3": "hard"}
        for key, value in difficulties.items():
            print(f"  {key}. {value}")

        diff_choice = input("选择难度 (1-3): ")
        difficulty = difficulties.get(diff_choice, "easy")

        # 执行创建命令
        cmd = f'"{PYTHON_EXE}" tools/new_leetcode.py --number {number} --title "{title}" --category {category} --difficulty {difficulty}'
        print(f"\n执行命令: {cmd}")
        os.system(cmd)

    except (ValueError, KeyboardInterrupt):
        print("❌ 输入无效或已取消")


def show_progress():
    """显示学习进度"""
    cmd = f'"{PYTHON_EXE}" tools/progress.py'
    os.system(cmd)


def open_recent_problems():
    """显示最近的题目"""
    algorithms_path = PROJECT_ROOT / "algorithms"
    if not algorithms_path.exists():
        print("📂 还没有任何题目")
        return

    print("\n🎯 最近的题目:")
    print("-" * 30)

    all_problems = []
    for category_dir in algorithms_path.iterdir():
        if category_dir.is_dir():
            for problem_dir in category_dir.iterdir():
                if problem_dir.is_dir() and problem_dir.name.startswith("LC"):
                    all_problems.append(problem_dir)

    # 按修改时间排序
    all_problems.sort(key=lambda x: x.stat().st_mtime, reverse=True)

    for i, problem_path in enumerate(all_problems[:10]):  # 显示最近10个
        print(f"{i+1:2d}. {problem_path.name}")

    if all_problems:
        try:
            choice = int(input(f"\n选择题目 (1-{min(len(all_problems), 10)}): ")) - 1
            if 0 <= choice < len(all_problems):
                selected = all_problems[choice]
                solution_file = selected / "solution.py"
                notes_file = selected / "notes.md"

                print(f"\n📂 题目目录: {selected}")
                print(f"📝 解题文件: {solution_file}")
                print(f"📓 笔记文件: {notes_file}")

                action = input("\n选择操作 (1=运行代码, 2=查看笔记, Enter=返回): ")
                if action == "1" and solution_file.exists():
                    os.system(f'cd "{selected}" && "{PYTHON_EXE}" solution.py')
                elif action == "2" and notes_file.exists():
                    os.system(f'start notepad "{notes_file}"')

        except (ValueError, IndexError):
            print("❌ 选择无效")


def open_usage_guide():
    """打开使用指南"""
    guide_path = PROJECT_ROOT / "docs" / "usage_guide.md"
    if guide_path.exists():
        os.system(f'start notepad "{guide_path}"')
    else:
        print("❌ 使用指南文件不存在")


def run_tests():
    """运行测试选项"""
    print("\n🔧 测试选项:")
    print("1. 运行所有题目的测试")
    print("2. 运行特定题目的测试")

    choice = input("选择 (1-2): ")

    if choice == "1":
        # 查找并运行所有solution.py
        algorithms_path = PROJECT_ROOT / "algorithms"
        if algorithms_path.exists():
            for category_dir in algorithms_path.iterdir():
                if category_dir.is_dir():
                    for problem_dir in category_dir.iterdir():
                        if problem_dir.is_dir():
                            solution_file = problem_dir / "solution.py"
                            if solution_file.exists():
                                print(f"\n🧪 测试 {problem_dir.name}...")
                                os.system(
                                    f'cd "{problem_dir}" && "{PYTHON_EXE}" solution.py'
                                )
    elif choice == "2":
        open_recent_problems()


def main():
    """主函数"""
    while True:
        try:
            show_menu()
            choice = input("请选择 (0-5): ").strip()

            if choice == "0":
                print("\n👋 再见！继续加油刷题！")
                break
            elif choice == "1":
                create_new_problem()
            elif choice == "2":
                show_progress()
            elif choice == "3":
                open_recent_problems()
            elif choice == "4":
                open_usage_guide()
            elif choice == "5":
                run_tests()
            else:
                print("❌ 无效选择，请重新输入")

            input("\n按回车键继续...")

        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")
            input("按回车键继续...")


if __name__ == "__main__":
    main()
