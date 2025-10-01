# PythonQuest - LeetCode刷题记录

🐍 LeetCode刷题记录，记录代码和做题思路。

## 🚨 AI助手工作指令

**重要提醒：当用户发送LeetCode题目时，AI助手必须：**
1. 🔥 **首先读取** `docs/ai_workflow.md` 文件
2. 🔥 **严格按照** 工作流程执行，不得偏离
3. 🔥 **禁止解答题目** - 只创建空白模板文件
4. 🔥 **禁止提供解题思路** - 保持解题部分完全空白

## 🎯 简化工作流程

### 📝 使用方法

直接在聊天框告诉我你要做的LeetCode题目，格式如下：

```
题目: 1. 两数之和
描述: 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出...
```

### ⚡ 自动化流程

1. **题目分析** → 我会分析题目属于哪个算法分类（数组、字符串、动态规划等）
2. **文件创建** → 自动创建对应目录和Python模板文件，包含：
   - `solution.py` - 空白的解题模板文件
   - `notes.md` - 包含完整题目描述、示例、约束条件，但解题思路部分空白
3. **索引更新** → 自动更新README中的题目分类索引，方便查找

### GitHub Copilot 优化配置

- **代码补全**：Tab键接受建议，Alt+] / Alt+[ 切换建议
- **智能注释**：输入 `#` 或 `"""` 时自动生成注释建议
- **多行建议**：Ctrl+Enter 查看多个解法建议
- **局部接受**：Ctrl+→ 只接受下一个单词
- **Chat功能**：Ctrl+I 打开内联聊天，直接在代码中对话

## 📚 LeetCode题目记录

### 数组 (Array)

- 1\. 两数之和: [`TwoSum_1.py`](algorithms/array/LC0001_Two_Sum/solution.py)
- 1518\. 换水问题: [`LC1518_Water_Bottles`](algorithms/array/LC1518_Water_Bottles/solution.py)

### 字符串 (String)

### 双指针 (Two Pointers)

### 链表 (Linked List)

### 栈与队列 (Stack & Queue)

### 树 (Tree)

### 动态规划 (Dynamic Programming)

- 120\. 三角形最小路径和: [`LC0120_Triangle`](algorithms/dynamic_programming/LC0120_Triangle/solution.py)

### 图 (Graph)

### 回溯 (Backtracking)

### 贪心 (Greedy)

### 排序与搜索 (Sort & Search)

### 位运算 (Bit Manipulation)

## � 项目结构

```
PythonQuest/
├── algorithms/                    # 算法题目按分类组织
│   ├── array/                    # 数组相关
│   │   └── LC0001_Two_Sum/       # 示例：两数之和
│   │       ├── solution.py       # 空白解题模板
│   │       └── notes.md          # 空白学习笔记
│   ├── string/                   # 字符串
│   ├── linked_list/              # 链表
│   ├── tree/                     # 树
│   ├── dynamic_programming/      # 动态规划
│   └── ...                      # 其他分类
└── README.md                     # 题目索引（本文件）
```

## 🤖 AI助手工作流程

当你发送LeetCode题目给我时，我会：

1. **🔍 分析题目类型**：

   - 判断属于哪个算法分类（数组、动态规划、树等）
   - 如果没有对应分类，会创建新的分类目录
2. **📂 创建文件结构**：

   ```
   algorithms/[分类]/LC[编号]_[题目名]/
   ├── solution.py    # 空白解题模板
   └── notes.md       # 包含题目描述、示例、约束，解题部分空白
   ```
3. **📋 更新索引**：

   - 在README.md对应分类下添加题目链接
   - 保持索引的整齐和易查找

### GitHub Copilot 使用技巧：

```python
# 1. 函数签名补全 - 输入函数名，Tab接受建议
def twoSum(self, nums: List[int], target: int) -> List[int]:

# 2. 注释驱动开发 - 写注释，让Copilot生成代码
# 使用哈希表存储数组元素和索引的映射关系
# 遍历数组，对每个元素计算target-num的补数
# 如果补数在哈希表中存在，返回两个索引

# 3. 多解法对比 - Alt+] / Alt+[ 切换不同实现方案
# 4. 测试用例生成 - 描述测试需求，生成测试代码
```

---

**🚀 准备好开始刷题了吗？直接告诉我你想做哪道LeetCode题目！**
