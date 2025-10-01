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

**为什么会无限循环？**
- `numBottles` 是固定的初始值
- 每次循环 `numEmpty` 都会增加固定值
- 导致 `numEmpty` 永远 >= `numExchange`

## 解法分析

### 时间复杂度

- **O(log n)**
- 每次兑换后，空瓶数量大约减少为原来的 `1/numExchange`
- 循环次数与 numBottles 呈对数关系

### 空间复杂度

- **O(1)**
- 只使用了几个变量：`total`、`numEmpty`、`newBottles`

### 优化思路

这道题还可以用数学公式直接计算：
```
总喝水数 = numBottles + (numBottles - 1) / (numExchange - 1)
```
但模拟法更直观易懂。

## 总结

### 解题心得

1. **模拟类问题的关键**：理清每一轮的状态变化
2. **变量命名很重要**：清晰的命名能避免逻辑错误
3. **循环不变量**：每轮循环后，空瓶数必须减少，否则会无限循环

### 知识点

- ✅ 循环模拟
- ✅ 整除和取余运算
- ✅ 状态转移

### 相关题目

- LeetCode 202. 快乐数（类似的模拟过程）
- LeetCode 292. Nim 游戏（数学规律）
