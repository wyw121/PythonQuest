# PythonQuest 使用指南

## 🎯 项目简介

PythonQuest 是一个专门为LeetCode刷题学习设计的工作区，帮助你记录解题过程、管理多种解法、追踪学习进度。

## 📁 目录结构说明

```
PythonQuest/
├── algorithms/              # 按算法分类的题目
│   ├── array/              # 数组相关
│   │   └── LC0001_Two_Sum/  # 具体题目目录
│   │       ├── solution.py  # 解题代码和测试
│   │       └── notes.md     # 学习笔记
│   ├── string/             # 字符串相关
│   ├── linked_list/        # 链表相关
│   ├── tree/               # 树相关
│   ├── dynamic_programming/ # 动态规划
│   └── graph/              # 图算法
├── templates/              # 题目模板
├── tools/                  # 工具脚本
├── docs/                   # 文档和进度记录
└── data_structures/        # 数据结构实现
```

## 🚀 快速开始

### 1. 创建新题目记录

```bash
# 基本用法
python tools/new_leetcode.py --number 1 --title "Two Sum" --category array --difficulty easy

# 完整参数
python tools/new_leetcode.py \
  --number 167 \
  --title "Two Sum II Input Array Is Sorted" \
  --category array \
  --difficulty easy \
  --slug "two-sum-ii-input-array-is-sorted"
```

**参数说明：**
- `--number, -n`: LeetCode题目编号
- `--title, -t`: 英文题目名称
- `--category, -c`: 算法分类 (array/string/linked_list/tree/dynamic_programming/graph)
- `--difficulty, -d`: 难度 (easy/medium/hard)
- `--slug, -s`: LeetCode URL slug (可选，会自动生成)

### 2. 解题流程

#### 第一步：阅读题目
1. 打开生成的 `notes.md` 文件
2. 从LeetCode复制题目描述、示例、约束条件到对应位置

#### 第二步：分析和实现
1. 在 `notes.md` 中记录解题思路分析
2. 打开 `solution.py` 开始实现解法
3. 运行测试验证正确性：`python solution.py`

#### 第三步：记录学习心得
1. 在 `notes.md` 中记录解题过程、遇到的问题、学到的知识点
2. 总结这道题的关键点和容易出错的地方

### 3. 查看学习进度

```bash
# 生成进度报告
python tools/progress.py
```

会显示：
- 总体完成情况
- 按难度分布统计
- 按分类分布统计
- 最近记录的题目

## 💡 最佳实践

### 解题代码组织

每个 `solution.py` 文件包含：

```python
class Solution:
    def method1(self, *args):
        """
        解法一：暴力解法（如果有）
        时间复杂度：O(n²)
        空间复杂度：O(1)
        """
        # 实现代码
        pass

    def method2(self, *args):
        """
        解法二：优化解法
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        # 实现代码
        pass

# 完整的单元测试
class TestSolution(unittest.TestCase):
    # 测试用例
```

### 学习笔记结构

`notes.md` 包含完整的学习记录：

```markdown
# LC0001. Two Sum

## 📋 题目信息
- LeetCode编号、难度、分类、链接

## 🎯 题目理解
- 题目描述、示例、约束条件

## 💡 解题过程
- 第一次尝试的思路和结果
- 优化过程和最终性能

## 🧠 知识点总结
- 涉及的数据结构和算法
- 学到的技巧和套路

## 🔗 相关题目
- 类似题目的链接

## 📝 总结反思
- 关键点、易错点、解题模式
```

## 🔧 VS Code 配置

工作区已配置：

### 快捷任务
- `Ctrl+Shift+P` → `Tasks: Run Task`
  - "运行当前Python文件"
  - "运行单元测试"
  - "创建新的LeetCode题目"

### 调试配置
- F5: 调试当前Python文件
- 支持单元测试调试

### 代码格式化
- 保存时自动格式化 (Black)
- 自动整理导入
- 行长度限制提醒

## 🎨 个性化定制

### 添加新的算法分类

修改 `tools/new_leetcode.py` 中的 `CATEGORIES` 字典：

```python
CATEGORIES = {
    "array": "数组",
    "string": "字符串",
    # ... 其他分类
    "backtracking": "回溯",  # 新增分类
}
```

然后创建对应目录：
```bash
mkdir algorithms/backtracking
```

### 自定义模板

编辑 `templates/leetcode_template.py` 来定制题目模板。

## 📊 进度追踪

### 自动统计
- 按完成状态分组（已完成/进行中/未开始）
- 按难度统计完成率
- 按算法分类统计覆盖度

### 数据导出
进度数据保存在 `docs/progress.json`，可用于：
- 生成个人学习报告
- 与其他工具集成
- 数据可视化

## 🔍 常见问题

### Q: 如何处理一题多解？
A: 在同一个 `Solution` 类中实现多个方法 (`method1`, `method2` 等)，每个方法对应一种解法。

### Q: 如何处理题目的多种变体？
A: 可以在同一目录下创建 `solution_v2.py` 等文件，或在notes中详细记录变体解法。

### Q: 如何备份学习记录？
A: 整个项目就是你的学习记录，建议：
- 使用 Git 版本控制
- 定期推送到 GitHub/GitLab
- 导出 `docs/progress.json` 作为备份

### Q: 题目编号重复怎么办？
A: 工具会自动检查并避免创建重复目录，如果需要重新整理，可以手动重命名文件夹。

## 🎯 学习建议

1. **坚持记录**：每道题都完整记录，包括错误的尝试
2. **定期复习**：利用 notes.md 的总结进行复习
3. **模式识别**：关注相似题目的解题模式
4. **性能对比**：记录不同解法的性能表现
5. **知识总结**：定期整理某一类题目的通用解法

---

Happy Coding! 🚀
