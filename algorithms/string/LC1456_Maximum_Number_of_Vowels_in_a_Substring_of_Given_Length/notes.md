# LeetCode 1456. 定长子串中元音的最大数目

## 题目信息
- **难度**: 中等
- **标签**: 字符串、滑动窗口
- **题目链接**: [https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
- **解题日期**: 2025年10月12日 - 2025年10月13日

## 题目描述

给你字符串 `s` 和整数 `k`。

请返回字符串 `s` 中长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母** 为（a, e, i, o, u）。

### 示例

**示例 1:**
```
输入: s = "abciiidef", k = 3
输出: 3
解释: 子字符串 "iii" 包含 3 个元音字母。
```

**示例 2:**
```
输入: s = "aeiou", k = 2
输出: 2
解释: 任意长度为 2 的子字符串都包含 2 个元音字母。
```

**示例 3:**
```
输入: s = "leetcode", k = 3
输出: 2
解释: "lee"、"eet" 和 "ode" 都包含 2 个元音字母。
```

**示例 4:**
```
输入: s = "rhythms", k = 4
输出: 0
解释: 字符串 s 中不含任何元音字母。
```

**示例 5:**
```
输入: s = "tryhard", k = 4
输出: 1
```

### 约束条件
- `1 <= s.length <= 10^5`
- `s` 由小写英文字母组成
- `1 <= k <= s.length`

---

## 解题过程

### 1. 思路分析

**问题拆解:**
- 需要在字符串中找到长度为 k 的子串
- 统计这个子串中的元音字母数量
- 返回所有可能子串中元音数量的最大值

**解法选择:**
- **方法1: 暴力法** - 遍历每个窗口，重新计算元音数量
- **方法2: 滑动窗口** - 利用窗口移动时的增量更新，避免重复计算

---

### 2. 方法1: 暴力法

#### 实现思路
对每个可能的起始位置，计算长度为 k 的子串中的元音数量。

#### 代码实现
```python
def maxVowels(self, s: str, k: int) -> int:
    a = ["a", "e", "i", "o", "u"]
    n = len(s)
    count = 0
    max_count = 0  # ⚠️ 注意：不要用 max，会覆盖内置函数
    
    # 遍历每个可能的窗口起始位置
    for i in range(0, n - k + 1):
        # 计算当前窗口的元音数量
        for j in range(k):
            if s[i + j] in a:
                count += 1
        max_count = max(max_count, count)
        count = 0  # 重置计数器
    
    return max_count
```

#### 复杂度分析
- **时间复杂度**: O(n × k)
  - 外层循环: n-k+1 次
  - 内层循环: k 次
  - 总共约 n × k 次操作
- **空间复杂度**: O(1)
  - 只使用了固定的几个变量

#### 缺点
- 每次都重新计算整个窗口，存在大量重复计算
- 当 k 很大时，性能较差

---

### 3. 方法2: 滑动窗口（优化解法）

#### 核心思想

**滑动窗口不是函数，而是一种算法思想！**

窗口移动时，只需要：
1. **减去** 左边移出窗口的元素影响
2. **加上** 右边进入窗口的元素影响

可视化示例（`s = "abciiidef", k = 3`）:
```
初始化: [a b c] i i i d e f  → count = 1 (只有a)
滑动1:  a [b c i] i i d e f  → 减去'a'(1), 加上'i'(1) → count = 1
滑动2:  a b [c i i] i d e f  → 减去'b'(0), 加上'i'(1) → count = 2
滑动3:  a b c [i i i] d e f  → 减去'c'(0), 加上'i'(1) → count = 3 ✅
```

#### 实现步骤

**步骤1: 初始化第一个窗口**
```python
window_value = 0
for i in range(k):
    if s[i] in "aeiou":
        window_value += 1
result = window_value
```

**步骤2: 滑动窗口**
```python
for i in range(k, len(s)):
    # 移除左边元素 s[i-k]
    if s[i - k] in "aeiou":
        window_value -= 1
    
    # 添加右边元素 s[i]
    if s[i] in "aeiou":
        window_value += 1
    
    # 更新最大值
    result = max(result, window_value)
```

#### 完整代码实现
```python
def maxVowels_sliding_window(self, s: str, k: int) -> int:
    def impact_of(char: str) -> int:
        """返回字符的元音贡献值"""
        return 1 if char in "aeiou" else 0
    
    # 初始化第一个窗口
    window_value = result = 0
    for i in range(k):
        window_value += impact_of(s[i])
    result = window_value
    
    # 滑动窗口
    for i in range(k, len(s)):
        window_value -= impact_of(s[i - k])  # 移除左边
        window_value += impact_of(s[i])       # 添加右边
        result = max(window_value, result)
        
        # 提前退出优化
        if result == k:
            return k
    
    return result
```

#### 复杂度分析
- **时间复杂度**: O(n)
  - 初始化窗口: O(k)
  - 滑动窗口: O(n-k)，每个元素只访问一次
  - 总计: O(n)
- **空间复杂度**: O(1)
  - 只使用了几个变量

#### 性能对比
```
对于 s 长度为 10000, k = 100:
- 暴力法: 10000 × 100 = 1,000,000 次操作
- 滑动窗口: 10000 次操作
- 性能提升: 100倍！
```

---

## 重点知识总结

### 🎯 核心知识点

#### 1. 变量命名陷阱 ⚠️

**问题：** 不要使用Python内置函数名作为变量名

```python
# ❌ 错误示范
max = 0
max = max(max, count)  # TypeError: 'int' object is not callable

# ✅ 正确做法
max_count = 0
max_count = max(max_count, count)
```

**常见的内置函数名（避免使用）：**
- `max`, `min`, `sum`, `len`, `range`
- `list`, `dict`, `set`, `tuple`, `str`, `int`, `float`
- `input`, `print`, `open`, `type`, `id`

#### 2. 滑动窗口算法模板 🔥

滑动窗口是一种**思想**，不是特定的函数！

**固定窗口模板：**
```python
def sliding_window_fixed(s, k):
    # 1. 初始化第一个窗口
    window_value = 计算初始窗口([0:k])
    result = window_value
    
    # 2. 滑动窗口（从位置k开始）
    for i in range(k, len(s)):
        # 移除左边元素（窗口左边界是 i-k）
        window_value -= impact_of(s[i - k])
        
        # 添加右边元素（窗口右边界是 i）
        window_value += impact_of(s[i])
        
        # 更新结果
        result = update(result, window_value)
    
    return result
```

**关键理解：**
- `i` 是右指针（当前遍历位置）
- `i - k` 是左指针（窗口左边界）
- 当前窗口范围: `[i-k+1, i]`（长度为k）

#### 3. 三元表达式（条件表达式）

```python
# 完整语法
值1 if 条件 else 值2

# ❌ 错误：缺少 else
return 1 if char in "aeiou"

# ✅ 正确：完整表达式
return 1 if char in "aeiou" else 0
```

#### 4. 内部辅助函数的使用

```python
def main_function(self, s: str, k: int) -> int:
    # 定义内部辅助函数
    def impact_of(char: str) -> int:
        return 1 if char in "aeiou" else 0
    
    # 使用辅助函数
    count = impact_of('a')  # 返回 1
```

**好处：**
- 代码模块化，逻辑清晰
- 避免重复代码
- 提高可读性

#### 5. 性能优化技巧：提前退出

```python
for i in range(k, len(s)):
    window_value -= impact_of(s[i - k])
    window_value += impact_of(s[i])
    result = max(window_value, result)
    
    # 🚀 优化：已达到理论最大值，提前返回
    if result == k:
        return k

return result
```

**原理：** 窗口大小为k，最多只能有k个元音，提前退出避免无意义的计算。

#### 6. 使用 set 优化查找性能

```python
# 方法1：使用列表（每次查找 O(5)）
vowels = ["a", "e", "i", "o", "u"]
if char in vowels:  # O(5) 线性查找

# 方法2：使用集合（每次查找 O(1)）
vowels = {"a", "e", "i", "o", "u"}
if char in vowels:  # O(1) 哈希查找

# 方法3：直接使用字符串（简洁）
if char in "aeiou":  # O(5)，但代码更简洁
```

对于元音只有5个，差别不大，但养成使用 `set` 的习惯很重要！

---

## 易错点总结

### ⚠️ 易错点1: 变量名覆盖内置函数
```python
# ❌ 错误
max = 0
result = max(a, b)  # TypeError

# ✅ 正确
max_count = 0
result = max(a, b)
```

### ⚠️ 易错点2: 三元表达式缺少 else
```python
# ❌ 错误
return 1 if condition  # SyntaxError

# ✅ 正确
return 1 if condition else 0
```

### ⚠️ 易错点3: 函数参数写法错误
```python
# ❌ 错误：不能用索引表达式作为参数
def func(s[i]: str):
    pass

# ✅ 正确：使用变量名
def func(char: str):
    pass
# 调用时传入 s[i] 的值
result = func(s[i])
```

### ⚠️ 易错点4: return 位置错误
```python
# ❌ 错误：return 在循环内，只执行一次
for i in range(n):
    result = process(i)
    return result  # 第一次循环就返回了

# ✅ 正确：return 在循环外
for i in range(n):
    result = process(i)
return result  # 循环完成后返回
```

### ⚠️ 易错点5: 滑动窗口边界理解错误
```python
# 窗口范围: [i-k+1, i]
for i in range(k, len(s)):  # i 是右边界
    left = i - k              # 移除的元素位置
    right = i                 # 添加的元素位置
```

---

## 学习收获

### ✅ 掌握的技能

1. **算法思想**
   - ✅ 理解滑动窗口的核心思想
   - ✅ 学会识别适合使用滑动窗口的题目
   - ✅ 掌握固定窗口的模板写法

2. **代码技巧**
   - ✅ 避免使用内置函数名作为变量名
   - ✅ 正确使用三元表达式
   - ✅ 使用内部辅助函数优化代码结构
   - ✅ 提前退出优化性能

3. **性能分析**
   - ✅ 理解时间复杂度 O(n×k) vs O(n) 的差异
   - ✅ 学会分析算法的性能瓶颈
   - ✅ 掌握性能优化的思路

4. **编程习惯**
   - ✅ 编写测试用例验证代码正确性
   - ✅ 对比不同解法的性能
   - ✅ 添加清晰的注释和文档

### 🚀 进阶方向

**相似题目推荐：**
- LeetCode 3. 无重复字符的最长子串（可变窗口）
- LeetCode 438. 找到字符串中所有字母异位词（固定窗口）
- LeetCode 567. 字符串的排列（固定窗口）
- LeetCode 76. 最小覆盖子串（可变窗口，困难）

**滑动窗口的其他应用场景：**
- 数组中的连续子数组问题
- 字符串匹配问题
- 限制条件下的最优解问题

---

## 代码实现对比

| 特性 | 暴力法 | 滑动窗口 |
|------|--------|----------|
| 时间复杂度 | O(n × k) | O(n) |
| 空间复杂度 | O(1) | O(1) |
| 代码长度 | 短 | 中等 |
| 代码难度 | 简单 | 中等 |
| 适用场景 | 小数据量 | 大数据量 |
| LeetCode性能 | 较慢 | 较快 |

**实际性能测试（n=10000, k=100）：**
- 暴力法: ~1000ms
- 滑动窗口: ~10ms
- **性能提升: 100倍**

---

**总结：** 这道题通过暴力法和滑动窗口的对比，深刻理解了算法优化的重要性。滑动窗口是面试高频考点，掌握其模板对后续刷题帮助很大！

**解题日期**: 2025年10月12日 - 2025年10月13日  
**学习时长**: 约2小时  
**掌握程度**: ⭐⭐⭐⭐⭐