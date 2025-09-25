#!/usr/bin/env python3
"""
LeetCode学习进度统计工具

功能：
1. 统计已完成的题目数量
2. 按分类和难度分组显示
3. 生成学习报告
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import re

PROJECT_ROOT = Path(__file__).parent.parent
ALGORITHMS_PATH = PROJECT_ROOT / "algorithms"

# 难度颜色映射
DIFFICULTY_COLORS = {"简单": "🟢", "中等": "🟡", "困难": "🔴"}

CATEGORY_NAMES = {
    "array": "数组",
    "string": "字符串",
    "linked_list": "链表",
    "tree": "树",
    "dynamic_programming": "动态规划",
    "graph": "图",
}


def scan_problems():
    """扫描所有题目并统计信息"""
    problems = []

    if not ALGORITHMS_PATH.exists():
        print("❌ algorithms目录不存在")
        return problems

    for category_dir in ALGORITHMS_PATH.iterdir():
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        for problem_dir in category_dir.iterdir():
            if not problem_dir.is_dir():
                continue

            # 解析题目编号和名称
            match = re.match(r"LC(\d{4})_(.+)", problem_dir.name)
            if not match:
                continue

            number = int(match.group(1))
            title = match.group(2).replace("_", " ")

            # 检查文件是否存在
            solution_file = problem_dir / "solution.py"
            notes_file = problem_dir / "notes.md"

            # 尝试获取难度信息
            difficulty = "未知"
            status = "未开始"

            if solution_file.exists():
                try:
                    content = solution_file.read_text(encoding="utf-8")
                    # 从文件中提取难度信息
                    diff_match = re.search(r"难度: (.+)", content)
                    if diff_match:
                        difficulty = diff_match.group(1).strip()

                    # 简单检查是否有实现（不仅仅是pass）
                    if "TODO" in content or content.count("pass") > 2:
                        status = "进行中"
                    else:
                        status = "已完成"
                except:
                    pass

            problems.append(
                {
                    "number": number,
                    "title": title,
                    "category": category,
                    "difficulty": difficulty,
                    "status": status,
                    "has_solution": solution_file.exists(),
                    "has_notes": notes_file.exists(),
                    "path": problem_dir,
                }
            )

    return sorted(problems, key=lambda x: x["number"])


def generate_statistics(problems):
    """生成统计信息"""
    stats = {
        "total": len(problems),
        "completed": len([p for p in problems if p["status"] == "已完成"]),
        "in_progress": len([p for p in problems if p["status"] == "进行中"]),
        "not_started": len([p for p in problems if p["status"] == "未开始"]),
        "by_category": defaultdict(lambda: {"total": 0, "completed": 0}),
        "by_difficulty": defaultdict(lambda: {"total": 0, "completed": 0}),
    }

    for problem in problems:
        category = problem["category"]
        difficulty = problem["difficulty"]
        is_completed = problem["status"] == "已完成"

        # 按分类统计
        stats["by_category"][category]["total"] += 1
        if is_completed:
            stats["by_category"][category]["completed"] += 1

        # 按难度统计
        stats["by_difficulty"][difficulty]["total"] += 1
        if is_completed:
            stats["by_difficulty"][difficulty]["completed"] += 1

    return stats


def print_progress_report(problems, stats):
    """打印进度报告"""
    print("=" * 60)
    print("🎯 LeetCode 学习进度报告")
    print("=" * 60)

    # 总体统计
    print(f"\n📊 总体进度:")
    print(f"   总题目数: {stats['total']}")
    print(f"   已完成: {stats['completed']} ✅")
    print(f"   进行中: {stats['in_progress']} 🔄")
    print(f"   未开始: {stats['not_started']} ⏳")

    if stats["total"] > 0:
        completion_rate = stats["completed"] / stats["total"] * 100
        print(f"   完成率: {completion_rate:.1f}%")

    # 按难度统计
    print(f"\n🎚️ 按难度分布:")
    for difficulty, data in stats["by_difficulty"].items():
        if data["total"] > 0:
            icon = DIFFICULTY_COLORS.get(difficulty, "⚪")
            rate = data["completed"] / data["total"] * 100
            print(
                f"   {icon} {difficulty}: {data['completed']}/{data['total']} ({rate:.1f}%)"
            )

    # 按分类统计
    print(f"\n📂 按分类分布:")
    for category, data in stats["by_category"].items():
        if data["total"] > 0:
            name = CATEGORY_NAMES.get(category, category)
            rate = data["completed"] / data["total"] * 100
            print(f"   📁 {name}: {data['completed']}/{data['total']} ({rate:.1f}%)")

    # 最近题目
    if problems:
        print(f"\n📋 最近记录的题目:")
        recent = sorted(problems, key=lambda x: x["number"], reverse=True)[:5]
        for problem in recent:
            icon = DIFFICULTY_COLORS.get(problem["difficulty"], "⚪")
            status_icon = {"已完成": "✅", "进行中": "🔄", "未开始": "⏳"}[
                problem["status"]
            ]
            print(
                f"   {status_icon} LC{problem['number']:04d}. {problem['title']} {icon}"
            )


def save_progress_json(problems, stats):
    """保存进度到JSON文件"""
    data = {
        "generated_at": str(Path().absolute()),
        "stats": stats,
        "problems": problems,
    }

    output_file = PROJECT_ROOT / "docs" / "progress.json"
    output_file.parent.mkdir(exist_ok=True)

    # 序列化Path对象
    for problem in data["problems"]:
        problem["path"] = str(problem["path"])

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 进度数据已保存到: {output_file}")


def main():
    print("🔍 扫描LeetCode题目...")
    problems = scan_problems()

    if not problems:
        print("📝 还没有创建任何题目记录。")
        print("💡 使用以下命令创建第一个题目:")
        print(
            '   python tools/new_leetcode.py --number 1 --title "Two Sum" --category array --difficulty easy'
        )
        return

    stats = generate_statistics(problems)
    print_progress_report(problems, stats)
    save_progress_json(problems, stats)

    print(f"\n🎉 加油继续刷题！")


if __name__ == "__main__":
    main()
