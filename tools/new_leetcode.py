#!/usr/bin/env python3
"""
LeetCode题目记录生成器

使用方法:
python tools/new_leetcode.py --number 1 --title "Two Sum" --category array
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "leetcode_template.py"

# 难度级别
DIFFICULTY_LEVELS = {"easy": "简单", "medium": "中等", "hard": "困难"}

# 算法分类
CATEGORIES = {
    "array": "数组",
    "string": "字符串",
    "linked_list": "链表",
    "tree": "树",
    "dynamic_programming": "动态规划",
    "graph": "图",
}


def create_leetcode_problem(
    number: int, title: str, category: str, difficulty: str, slug: str = ""
):
    """创建LeetCode题目记录文件夹和文件"""

    # 验证参数
    if category not in CATEGORIES:
        print(f"❌ 无效的分类: {category}")
        print(f"✅ 支持的分类: {', '.join(CATEGORIES.keys())}")
        return False

    if difficulty not in DIFFICULTY_LEVELS:
        print(f"❌ 无效的难度: {difficulty}")
        print(f"✅ 支持的难度: {', '.join(DIFFICULTY_LEVELS.keys())}")
        return False

    # 创建文件夹
    category_path = PROJECT_ROOT / "algorithms" / category
    safe_title = "".join(c if c.isalnum() or c in "._-" else "_" for c in title)
    folder_name = f"LC{number:04d}_{safe_title}"
    problem_path = category_path / folder_name

    problem_path.mkdir(exist_ok=True)
    print(f"📁 创建LeetCode题目目录: {problem_path}")

    # 读取模板
    if not TEMPLATE_PATH.exists():
        print(f"❌ 模板文件不存在: {TEMPLATE_PATH}")
        return False

    template_content = TEMPLATE_PATH.read_text(encoding="utf-8")

    # 生成URL slug
    if not slug:
        slug = title.lower().replace(" ", "-")

    # 填充解题文件模板
    content = template_content.format(
        leetcode_title=title,
        problem_number=number,
        difficulty=DIFFICULTY_LEVELS[difficulty],
        problem_slug=slug,
        solve_date=datetime.now().strftime("%Y-%m-%d"),
    )

    # 创建解题文件
    solution_file = problem_path / "solution.py"
    solution_file.write_text(content, encoding="utf-8")
    print(f"📝 创建解题文件: {solution_file}")

    # 创建学习笔记
    notes_content = f"""# LC{number:04d}. {title}

## 📋 题目信息
- **LeetCode编号**: {number}
- **题目名称**: {title}
- **难度**: {DIFFICULTY_LEVELS[difficulty]}
- **分类**: {CATEGORIES[category]}
- **题目链接**: https://leetcode.cn/problems/{slug}/
- **开始时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}

## 🎯 题目理解

### 题目描述
<!-- 从LeetCode复制题目描述 -->

### 示例
<!-- 从LeetCode复制示例 -->

### 约束条件
<!-- 从LeetCode复制约束条件 -->

## 💡 解题过程

### 第一次尝试
- **开始时间**:
- **解题思路**:
- **遇到的问题**:
- **是否通过**:
- **用时**:
- **内存消耗**:

### 优化过程
- **优化思路**:
- **改进点**:
- **最终性能**:
  - 时间复杂度: O()
  - 空间复杂度: O()
  - 执行用时:
  - 内存消耗:

## 🧠 知识点总结

### 涉及的数据结构

### 涉及的算法

### 学到的技巧

## 🔗 相关题目
-
-
-

## 📝 总结反思

### 这道题的关键点

### 容易出错的地方

### 下次遇到类似题目的思路
"""

    notes_file = problem_path / "notes.md"
    notes_file.write_text(notes_content, encoding="utf-8")
    print(f"📓 创建学习笔记: {notes_file}")

    print(f"\n✅ LeetCode {number}. {title} 记录创建成功!")
    print(f"📂 位置: {problem_path}")
    print("🎯 下一步:")
    print("   1. 去LeetCode复制题目描述到 notes.md")
    print("   2. 在 solution.py 中实现解法")
    print("   3. 记录解题过程和心得")

    return True


def main():
    parser = argparse.ArgumentParser(description="创建LeetCode题目记录")
    parser.add_argument(
        "--number", "-n", type=int, required=True, help="LeetCode题目编号"
    )
    parser.add_argument("--title", "-t", required=True, help="题目英文名称")
    parser.add_argument(
        "--category", "-c", required=True, help="题目分类", choices=CATEGORIES.keys()
    )
    parser.add_argument(
        "--difficulty",
        "-d",
        required=True,
        help="难度级别",
        choices=DIFFICULTY_LEVELS.keys(),
    )
    parser.add_argument("--slug", "-s", default="", help="LeetCode URL slug (可选)")

    args = parser.parse_args()

    success = create_leetcode_problem(
        number=args.number,
        title=args.title,
        category=args.category,
        difficulty=args.difficulty,
        slug=args.slug,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
