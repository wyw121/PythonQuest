# LeetCode 407. 接雨水 II

## 题目描述

给你一个 `m x n` 的矩阵,其中的值均为非负整数,代表二维高度图每个单元的高度,请计算图中形状最多能接多少体积的雨水。

## 示例

### 示例 1:

```
输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后,雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
```

### 示例 2:

```
输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10
```

## 约束条件

- `m == heightMap.length`
- `n == heightMap[i].length`
- `1 <= m, n <= 200`
- `0 <= heightMap[i][j] <= 2 * 10^4`

---

## 解题过程

### 1. 理解题意

这是一个二维接雨水问题，核心思想是：
- **边界永远是"出水口"**，边界上的格子无论多高都不能存水
- 每个内部格子能存的水，取决于它**到边界的最优路径**中的"最高点"
- 使用**优先队列(最小堆) + BFS**从边界向内逐步扩散

**关键洞察：**
- 水位不是由直接邻居决定，而是由到边界的最容易流走的路径决定
- 从边界的最低点开始处理，保证每个格子第一次被访问时就是通过最优路径

### 2. 解法分析

#### 核心算法：优先队列 + BFS

**算法步骤：**

```python
# 1. 边界入堆
for 边界格子:
    堆.push((高度, 行, 列))
    标记为已访问

# 2. BFS 扩散
while 堆不为空:
    当前水位, 行, 列 = 堆.pop()  # 取最小
    
    for 四个方向的邻居:
        if 邻居有效 且 未访问:
            邻居水位 = max(当前水位, 邻居高度)
            蓄水量 = 邻居水位 - 邻居高度
            总水量 += 蓄水量
            堆.push((邻居水位, 邻居坐标))
            标记邻居已访问
```

**为什么这样做？**
- 总是处理最低水位的格子 → 保证找到最优路径
- 水位传播：从边界 → 内部，逐步提高
- 每个格子的水位 = max(到达它的水位, 自身高度)

---

## 📚 四种实现方法对比

本题我实现了 **4 种不同的解法**，都在 `solution.py` 中：

| 方法 | 推荐度 | 空间复杂度 | 核心特点 | 适用场景 |
|------|--------|-----------|---------|---------|
| `Solution` | ⭐⭐⭐⭐⭐ | O(m×n) | 我的原始版本，清晰易懂 | 学习理解 |
| `SolutionOptimized` | ⭐⭐⭐⭐⭐ | O(m×n) | 添加边界检查，更健壮 | 实际应用 |
| `SolutionMemoryOptimized` | ⭐⭐⭐⭐ | **O(1)** ✨ | 极致空间优化 | 竞赛/面试 |
| `SolutionAlternative` | ⭐⭐⭐ | O(m×n) | 使用set代替数组 | 了解即可 |

### 方法1: Solution (我的原始版本)

**核心代码：**
```python
visited = [[False] * n for _ in range(m)]  # 二维数组标记
neighbor_water_level = max(water_level, neighbor_height)
water_stored = neighbor_water_level - neighbor_height
total_water += water_stored
```

**优点：**
- ✅ 变量命名清晰（易于理解）
- ✅ 逻辑完整，适合学习
- ✅ 代码可读性强

**复杂度：**
- 时间：O(m×n×log(m×n))
- 空间：O(m×n)

---

### 方法2: SolutionOptimized (标准优化版)

**改进点：**
```python
# 1. 边界检查
if not heightMap or not heightMap[0]:
    return 0

# 2. 特殊情况处理
if m < 3 or n < 3:
    return 0

# 3. 使用更快的边界判断
if 0 <= new_row < m and 0 <= new_col < n:  # 而不是 in range()
```

**优点：**
- ✅ 更健壮，处理边界情况
- ✅ 性能略优
- ✅ 代码规范，适合工程

**推荐场景：** 实际项目、LeetCode提交

---

### 方法3: SolutionMemoryOptimized (内存优化版) ⭐⭐⭐

这是**最优化的版本**！

**核心优化技巧：**

#### ① 原地标记 - 最重要的优化！
```python
# 传统做法：额外 O(m×n) 空间
visited = [[False] * n for _ in range(m)]

# 优化做法：0 额外空间！
heightMap[i][j] = -1  # 用 -1 表示已访问
if heightMap[x][y] >= 0:  # >= 0 表示未访问
```

**节省：** 200×200 矩阵约 40KB 内存！

#### ② heapify 优化
```python
# 慢: O(n log n)
for item in items:
    heapq.heappush(heap, item)

# 快: O(n)
heap = list(items)
heapq.heapify(heap)
```

**快约 2-3 倍！**

**优点：**
- ✅ 空间复杂度：O(m×n) → **O(1)**
- ✅ 初始化更快
- ✅ 代码更简洁

**缺点：**
- ⚠️ 修改了输入数组
- ⚠️ 依赖题目条件（高度非负）

**复杂度：**
- 时间：O(m×n×log(m×n))
- 空间：**O(1)** (不计堆)

**推荐场景：** 面试炫技、竞赛

---

### 方法4: SolutionAlternative (Set版本)

```python
visited = set()  # 用 set 代替二维数组
visited.add((i, j))
if (nx, ny) not in visited:
```

**特点：**
- 使用 set 存储坐标
- 更 Pythonic

**缺点：**
- set 查找比数组索引稍慢

---

## 📊 性能对比

### 空间复杂度对比

| 版本 | visited | 堆 | 总计 |
|------|---------|-----|------|
| Solution | O(m×n) | O(m+n) | O(m×n) |
| SolutionOptimized | O(m×n) | O(m+n) | O(m×n) |
| **MemoryOptimized** | **0** ✨ | O(m+n) | **O(1)** ✨ |
| Alternative | O(m×n) | O(m+n) | O(m×n) |

### 时间复杂度对比

| 操作 | 我的版本 | 内存优化版 |
|------|---------|-----------|
| 初始化堆 | O(k log k) | **O(k)** ✨ |
| BFS处理 | O(mn log(mn)) | O(mn log(mn)) |
| **总计** | O(mn log(mn)) | O(mn log(mn)) |

*k = 边界数 ≈ 2(m+n)*

---

## 💯 我的代码评价

### 总体评分：94/100 🎉

| 维度 | 得分 | 评价 |
|------|------|------|
| 算法正确性 | ⭐⭐⭐⭐⭐ | 核心逻辑完全正确 |
| 时间复杂度 | ⭐⭐⭐⭐⭐ | 与标准答案一致 |
| 空间复杂度 | ⭐⭐⭐⭐⭐ | 标准做法 |
| 代码简洁性 | ⭐⭐⭐⭐ | 清晰但可优化 |
| 可读性 | ⭐⭐⭐⭐⭐ | 变量命名清晰 |
| 鲁棒性 | ⭐⭐⭐⭐ | 缺少边界检查 |

### ✅ 做得好的地方

1. **核心算法完全正确**
   ```python
   neighbor_water_level = max(water_level, neighbor_height)
   water_stored = neighbor_water_level - neighbor_height
   ```

2. **数据结构选择正确**
   - ✅ 小根堆 heapq
   - ✅ 二维数组 visited
   - ✅ 方向数组 directions

3. **代码逻辑清晰**
   - 变量命名合理
   - 流程清晰易懂

### 💡 可优化的地方

1. **边界检查**
   ```python
   # 优化前
   m = len(heightMap)
   
   # 优化后
   if not heightMap or not heightMap[0]:
       return 0
   ```

2. **边界判断方式**
   ```python
   # 优化前（稍慢）
   if new_row in range(m):
   
   # 优化后（更快）
   if 0 <= new_row < m:
   ```

3. **可选：简化变量名**
   ```python
   # 当前（清晰）
   neighbor_water_level = max(water_level, neighbor_height)
   
   # 可简化（简洁）
   level = max(water_level, height)
   ```

---

## 总结

### 🎯 核心知识点

1. **优先队列 + BFS**
   - 从边界最低点开始
   - 总是处理最低水位
   - 逐步向内扩散

2. **水位传播机制**
   - 邻居水位 = max(当前水位, 邻居高度)
   - 蓄水量 = 水位 - 高度
   - 单向传播：已处理 → 未处理

3. **优化技巧**
   - 原地标记：用特殊值代替 visited
   - heapify：批量建堆更快
   - 边界检查：提高健壮性

### 🔑 关键点

- ✅ 边界是出水口，从边界开始处理
- ✅ 总是选最低水位处理（贪心）
- ✅ 每个格子的水位由最优路径决定
- ✅ 堆里存的是**水位**，不是高度

### ⚠️ 易错点

- ❌ 不要只看四周邻居判断水位
- ❌ 入堆时存水位，不是高度
- ❌ 不要忘记边界检查
- ❌ 原地标记要注意修改输入

### 🚀 优化思路

1. **空间优化**：原地标记 O(m×n) → O(1)
2. **时间优化**：heapify 代替多次 push
3. **健壮性**：添加边界和特殊情况检查

### 📚 相关题目

- LeetCode 42. 接雨水（一维版本）
- LeetCode 1499. 满足不等式的最大值
- Dijkstra 最短路径算法
- Prim 最小生成树算法

### 🎓 学习收获

1. ✅ 独立完成困难题
2. ✅ 掌握优先队列应用
3. ✅ 理解贪心 + BFS 思想
4. ✅ 学会多种优化技巧

---

**解题日期：** 2025年10月3日  
**代码文件：** `solution.py`（包含4种实现）  
**测试状态：** ✅ 所有测试通过
