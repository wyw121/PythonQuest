# AI助手工作流程指南

## 🎯 当用户提供LeetCode题目时的标准流程

### 1. 题目信息提取
从用户消息中提取：
- 题目编号
- 题目名称（中文和英文）
- 题目描述
- 示例（包含输入输出和解释）
- 约束条件
- 进阶要求（如果有）

### 2. 题目分类判断
根据题目特征判断算法分类：
- array（数组）
- string（字符串） 
- linked_list（链表）
- tree（树）
- dynamic_programming（动态规划）
- graph（图）
- 其他分类...

### 3. 创建文件结构
```
algorithms/[分类]/LC[编号]_[英文名]/
├── solution.py    # 空白解题模板
└── notes.md       # 部分填写的笔记模板
```

### 4. 填写内容规则

#### solution.py - 保持完全空白
```python
"""
LeetCode题目: [题目英文名]
题目编号: [编号]
难度: [难度]
题目链接: https://leetcode.cn/problems/[slug]/

解题日期: [当前日期]
"""

import unittest
from typing import List, Optional


class Solution:
    def solve(self, *args):
        """
        解题方法
        """
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试用例"""
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

#### notes.md - 填写题目信息，保持解题部分空白
**需要填写的部分：**
- ✅ 题目描述（完整复制）
- ✅ 示例（包含输入输出和解释）
- ✅ 约束条件（数据范围等）
- ✅ 进阶要求（如果有）

**保持空白的部分：**
- 🔲 解题过程
- 🔲 解法分析
- 🔲 总结部分

### 5. 更新README索引
在对应分类下添加题目链接：
```markdown
- [编号]\. [中文题目名]: [`LC[编号]_[英文名]`](algorithms/[分类]/LC[编号]_[英文名]/solution.py)
```

## 🚫 注意事项

1. **绝对不要**填写具体的解题代码实现
2. **绝对不要**填写解题思路和分析
3. **绝对不要**填写性能数据和总结
4. **只填写**题目本身的基础信息
5. **确保**README索引得到更新

## ✅ 完成标准

- [ ] 创建了正确的文件夹结构
- [ ] solution.py为空白模板
- [ ] notes.md包含完整题目信息
- [ ] notes.md的解题部分保持空白
- [ ] 更新了README索引
- [ ] 向用户确认完成