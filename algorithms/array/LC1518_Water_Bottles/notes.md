# LeetCode 1518. 换水问题

## 题目描述

超市正在促销，你可以用 numExchange 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 numBottles 瓶水。

如果喝掉了水瓶中的水，那么水瓶就会变成空的。

给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。

## 示例

### 示例 1：

输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空瓶兑换 1 瓶水。
所以最多能喝到 9 + 3 + 1 = 13 瓶水。

### 示例 2：

输入：numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空瓶兑换 1 瓶水。
所以最多能喝到 15 + 3 + 1 = 19 瓶水。

## 约束条件

- 1 <= numBottles <= 100
- 2 <= numExchange <= 100

## 解题过程

### 思路分析

这是一道模拟题，核心思路是**循环模拟兑换过程**：

1. **初始状态**：
   - 总喝水数 = numBottles（初始购买的水）
   - 空瓶数 = numBottles（喝完后都变成空瓶）

2. **循环条件**：
   - 当空瓶数 >= numExchange 时，可以继续兑换

3. **循环操作**：
   - 计算本轮能兑换的新水瓶数：`newBottles = numEmpty // numExchange`
   - 累加总喝水数：`total += newBottles`
   - 更新空瓶数：`numEmpty = numEmpty % numExchange + newBottles`
     - `numEmpty % numExchange`：剩余无法兑换的空瓶
     - `+ newBottles`：新得到的水喝完后的空瓶

### 算法步骤

以示例1为例：numBottles = 9, numExchange = 3

```
初始：total = 9, numEmpty = 9

第1轮循环：9 >= 3 ✓
  - newBottles = 9 // 3 = 3
  - total = 9 + 3 = 12
  - numEmpty = 9 % 3 + 3 = 0 + 3 = 3

第2轮循环：3 >= 3 ✓
  - newBottles = 3 // 3 = 1
  - total = 12 + 1 = 13
  - numEmpty = 3 % 3 + 1 = 0 + 1 = 1

第3轮：1 < 3 ✗ 退出循环

最终结果：13
```

### 代码实现

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles  # 记录总共喝了多少瓶水
        numEmpty = numBottles  # 当前空瓶数
        
        while numEmpty >= numExchange:
            newBottles = numEmpty // numExchange  # 本轮兑换得到的新瓶数
            total += newBottles
            numEmpty = numEmpty % numExchange + newBottles  # 更新空瓶数
            
        return total
```

### 易错点

⚠️ **常见错误**：使用初始的 `numBottles` 而不是 `newBottles`

```python
# ❌ 错误写法
numEmpty = numEmpty % numExchange + numBottles  # 会导致无限循环！

# ✅ 正确写法
numEmpty = numEmpty % numExchange + newBottles  # 使用本轮兑换得到的新瓶数
```

---

## 多种解法对比

### 方法1: 模拟法（迭代循环）⭐ 最直观

**时间复杂度**: O(log n)  
**空间复杂度**: O(1)

```python
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    total = numBottles
    numEmpty = numBottles
    while numEmpty >= numExchange:
        newBottles = numEmpty // numExchange
        total += newBottles
        numEmpty = numEmpty % numExchange + newBottles
    return total
```

**优点**: 逻辑清晰，易于理解  
**缺点**: 需要循环，不是常数时间

---

### 方法2: 数学公式法 ⭐⭐⭐ 最优解

**时间复杂度**: O(1) 🚀  
**空间复杂度**: O(1)

```python
def numWaterBottles_math(self, numBottles: int, numExchange: int) -> int:
    if numBottles < numExchange:
        return numBottles
    return numBottles + (numBottles - 1) // (numExchange - 1)
```

**核心思想**:
- 每次兑换：用 `numExchange` 个空瓶 → 得到 1 瓶水（喝完又是 1 个空瓶）
- **本质**：相当于用 `numExchange - 1` 个空瓶"消耗"掉，换来 1 瓶可喝的水
- 初始有 `numBottles` 个空瓶可用于兑换
- 最多能兑换 `(numBottles - 1) // (numExchange - 1)` 次

**为什么分子是 `numBottles - 1`？** 🤔
- 兑换过程最后**一定会剩下至少 1 个空瓶**无法兑换
- 例如：4 个空瓶，需要 3 个才能兑换
  - 3 个空瓶 → 1 瓶水 → 喝完后 1 个空瓶
  - 现在有 1 + 1 = 2 个空瓶，无法继续兑换
  - 只能兑换 1 次
- 公式：`(4 - 1) / (3 - 1) = 3 / 2 = 1` ✓
- 本质：**可用于兑换的空瓶数 = numBottles - 1**（保留1个作为剩余）

**推导过程**（以 numBottles=9, numExchange=3 为例）:
```
初始: 喝了 9 瓶，有 9 个空瓶
每次兑换: 3 个空瓶 -> 1 瓶水 -> 1 个空瓶
相当于: 每次用 2 个空瓶换 1 瓶水

最多兑换次数 = (9 - 1) / (3 - 1) = 8 / 2 = 4 次
总喝水数 = 9 + 4 = 13 ✓
```

**优点**: 常数时间，效率最高  
**缺点**: 公式不够直观，需要理解推导过程

---

### 方法3: 递归法

**时间复杂度**: O(log n)  
**空间复杂度**: O(log n) - 递归栈空间

```python
def numWaterBottles_recursive(self, numBottles: int, numExchange: int) -> int:
    def helper(empty_bottles):
        if empty_bottles < numExchange:
            return 0
        new_bottles = empty_bottles // numExchange
        remaining = empty_bottles % numExchange
        return new_bottles + helper(new_bottles + remaining)
    
    return numBottles + helper(numBottles)
```

**递归逻辑**:
- 基本情况：空瓶数 < numExchange，无法兑换，返回 0
- 递归情况：计算本轮兑换数 + 递归处理剩余空瓶

**优点**: 代码简洁，符合函数式编程风格  
**缺点**: 占用递归栈空间，效率不如迭代

---

### 方法4: 优化模拟法（简化版本）

**时间复杂度**: O(log n)  
**空间复杂度**: O(1)

```python
def numWaterBottles_optimized(self, numBottles: int, numExchange: int) -> int:
    total = 0
    empty = 0
    
    while numBottles > 0:
        total += numBottles      # 喝掉所有满瓶
        empty += numBottles      # 增加空瓶数
        numBottles = empty // numExchange  # 能兑换的新瓶数
        empty = empty % numExchange        # 剩余空瓶
    
    return total
```

**优点**: 逻辑更清晰，"边喝边兑换"的思路  
**缺点**: 与方法1类似，需要循环

---

## 方法选择建议

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| **面试推荐** | 方法2 (数学公式) | O(1)时间，体现数学思维 |
| **初学者** | 方法1 (模拟法) | 最直观易懂 |
| **追求性能** | 方法2 (数学公式) | 常数时间最优 |
| **代码简洁** | 方法3 (递归) | 代码最短 |

---

## 关键知识点

1. **模拟法**: 适用于过程清晰的问题
2. **数学优化**: 找到规律可以将 O(log n) 优化到 O(1)
3. **整数除法**: `//` 和 `%` 的配合使用
4. **递归思维**: 将问题分解为更小的子问题

---

## 相关题目

- LeetCode 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？（数学计算）
- LeetCode 1763. 最长的美好子字符串（模拟）
- LeetCode 202. 快乐数（类似的模拟过程）
- LeetCode 292. Nim 游戏（数学规律）

---

## 总结

### 核心要点

1. **模拟法（方法1）**: 最直观，适合初学者理解
2. **数学公式法（方法2）**: O(1) 最优解，面试推荐
3. **递归法（方法3）**: 代码简洁，但占用栈空间
4. **优化模拟法（方法4）**: 逻辑清晰的迭代版本

### 关键难点

⚠️ **数学公式中的 `-1`**：
- `(numBottles - 1) // (numExchange - 1)`
- 分子 `-1`：最后一定剩至少 1 个空瓶无法兑换
- 分母 `-1`：每次兑换净消耗 `numExchange - 1` 个空瓶

### 解题心得

1. **模拟类问题的关键**：理清每一轮的状态变化
2. **数学优化**：通过找规律将 O(log n) 优化到 O(1)
3. **变量命名很重要**：清晰的命名能避免逻辑错误（如 `newBottles` vs `numBottles`）
4. **循环不变量**：每轮循环后，空瓶数必须减少，否则会无限循环

### 知识点标签

- ✅ 循环模拟
- ✅ 数学公式推导
- ✅ 递归思维
- ✅ 整除和取余运算
- ✅ 时间复杂度优化
