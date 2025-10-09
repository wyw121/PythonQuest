"""
LeetCode题目: Trapping Rain Water II
题目编号: 407
难度: 困难
题目链接: https://leetcode.cn/problems/trapping-rain-water-ii/

解题日期: 2025年10月3日

核心算法：优先队列(最小堆) + BFS
时间复杂度: O(m*n*log(m*n))
空间复杂度: O(m*n)

本文件包含 4 种不同的实现方式，按推荐程度排序：
1. Solution (我的原始版本) - 清晰易懂，适合学习
2. SolutionOptimized - 添加边界检查，更健壮
3. SolutionMemoryOptimized - 内存优化版本，空间复杂度 O(1)
4. SolutionAlternative - 使用 set 代替二维数组
"""

import unittest
import heapq
from typing import List


# =====================================================================
# 方法1: 我的原始版本 (最推荐用于理解算法)
# =====================================================================
class Solution:
    """
    我的原始实现版本
    
    优点:
    - 变量命名清晰，易于理解
    - 逻辑完整，核心算法正确
    - 代码可读性强
    
    特点:
    - 使用二维数组 visited 标记访问状态
    - 使用 in range() 判断边界
    - 每次 heappush 添加边界格子
    
    时间复杂度: O(m*n*log(m*n))
    空间复杂度: O(m*n)
    """
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        total_water = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 初始化：边界入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # BFS 扩散
        while heap:
            water_level, row, col = heapq.heappop(heap)
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (
                    new_row in range(m)
                    and new_col in range(n)
                    and not visited[new_row][new_col]
                ):
                    neighbor_height = heightMap[new_row][new_col]
                    neighbor_water_level = max(water_level, neighbor_height)
                    water_stored = neighbor_water_level - neighbor_height
                    total_water += water_stored
                    heapq.heappush(heap, (neighbor_water_level, new_row, new_col))
                    visited[new_row][new_col] = True
        
        return total_water


# =====================================================================
# 方法2: 优化版本 (推荐用于实际应用)
# =====================================================================
class SolutionOptimized:
    """
    标准优化版本
    
    改进点:
    1. 添加边界检查 (防止空输入)
    2. 添加特殊情况处理 (太小的矩阵)
    3. 使用 0 <= x < n 代替 in range() (性能更好)
    4. 添加详细注释
    
    优点:
    - 更健壮，能处理边界情况
    - 性能略优于原始版本
    - 代码规范，适合工程使用
    
    时间复杂度: O(m*n*log(m*n))
    空间复杂度: O(m*n)
    """
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 边界检查
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        # 特殊情况：太小的矩阵无法存水
        if m < 3 or n < 3:
            return 0
        
        # 最小堆: (水位, 行, 列)
        min_heap = []
        # 访问标记
        visited = [[False] * n for _ in range(m)]
        
        # 1. 初始化：将所有边界加入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # 四个方向：上下左右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_water = 0
        
        # 2. BFS 扩散
        while min_heap:
            # 取出当前最低水位的格子
            water_level, row, col = heapq.heappop(min_heap)
            
            # 检查四个方向的邻居
            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                
                # 边界检查和访问检查
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # 邻居的高度
                    height = heightMap[nx][ny]
                    
                    # 邻居的水位 = max(当前水位, 邻居高度)
                    neighbor_level = max(water_level, height)
                    
                    # 能存的水 = 水位 - 地面高度
                    total_water += neighbor_level - height
                    
                    # 将邻居加入堆，传播水位
                    heapq.heappush(min_heap, (neighbor_level, nx, ny))
                    visited[nx][ny] = True
        
        return total_water


# =====================================================================
# 方法3: 内存优化版本 (空间复杂度最优)
# =====================================================================
class SolutionMemoryOptimized:
    """
    内存优化版本 - 最省空间！
    
    核心优化:
    - 原地标记：用 -1 标记已访问，不需要额外的 visited 数组
    - heapify：一次性建堆，而不是多次 heappush
    
    优点:
    - 空间复杂度从 O(m*n) 降到 O(1) (不计堆的空间)
    - 初始化更快 (heapify 是 O(n)，多次 push 是 O(n log n))
    - 代码更简洁
    
    缺点:
    - 修改了输入数组 (破坏性操作)
    - 依赖题目条件 (高度必须非负)
    - 可读性稍差
    
    适用场景:
    - 面试/竞赛 (体现优化意识)
    - 内存受限的场景
    
    时间复杂度: O(m*n*log(m*n))
    空间复杂度: O(1) (不计堆的 O(m+n) 空间)
    """
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        if m < 3 or n < 3:
            return 0
        
        # 收集边界，用列表而不是立即入堆
        h = []
        for i, row in enumerate(heightMap):
            for j, height in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    h.append((height, i, j))
                    row[j] = -1  # 原地标记：用 -1 表示已访问
        
        # 一次性建堆 (O(n) 比多次 push 的 O(n log n) 更快)
        heapq.heapify(h)
        
        ans = 0
        
        # BFS 扩散
        while h:
            min_height, i, j = heapq.heappop(h)
            
            # 直接在循环中生成四个方向的坐标
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                # heightMap[x][y] >= 0 表示未访问
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] >= 0:
                    # 计算蓄水量
                    ans += max(min_height - heightMap[x][y], 0)
                    # 传播水位
                    heapq.heappush(h, (max(min_height, heightMap[x][y]), x, y))
                    # 标记已访问
                    heightMap[x][y] = -1
        
        return ans


# =====================================================================
# 方法4: 使用 set 的替代版本
# =====================================================================
class SolutionAlternative:
    """
    使用 set 代替二维数组的版本
    
    特点:
    - 用 set 存储访问过的坐标 (i, j)
    - 代码更 Pythonic
    
    优点:
    - 不需要预先分配 m*n 的空间
    - 适合稀疏访问的场景
    
    缺点:
    - set 的哈希查找比数组索引稍慢
    - 坐标元组需要额外的对象开销
    
    时间复杂度: O(m*n*log(m*n))
    空间复杂度: O(m*n)
    """
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        if m < 3 or n < 3:
            return 0
        
        heap = []
        visited = set()  # 使用 set 代替二维数组
        
        # 边界入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        result = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            h, x, y = heapq.heappop(heap)
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    result += max(0, h - heightMap[nx][ny])
                    heapq.heappush(heap, (max(h, heightMap[nx][ny]), nx, ny))
                    visited.add((nx, ny))
        
        return result


# =====================================================================
# 测试代码 - 测试所有版本
# =====================================================================
class TestSolution(unittest.TestCase):
    """统一测试所有实现版本"""
    
    def setUp(self):
        """初始化所有版本"""
        self.solution = Solution()
        self.solution_opt = SolutionOptimized()
        self.solution_mem = SolutionMemoryOptimized()
        self.solution_alt = SolutionAlternative()
    
    def test_example1(self):
        """示例1: 基本测试"""
        heightMap = [[1, 4, 3, 1, 3, 2], 
                     [3, 2, 1, 3, 2, 4], 
                     [2, 3, 3, 2, 3, 1]]
        expected = 4
        
        self.assertEqual(self.solution.trapRainWater(heightMap), expected)
        self.assertEqual(self.solution_opt.trapRainWater(heightMap), expected)
        # 注意：内存优化版本会修改输入，需要重新创建
        heightMap_copy = [[1, 4, 3, 1, 3, 2], 
                          [3, 2, 1, 3, 2, 4], 
                          [2, 3, 3, 2, 3, 1]]
        self.assertEqual(self.solution_mem.trapRainWater(heightMap_copy), expected)
        self.assertEqual(self.solution_alt.trapRainWater(heightMap), expected)
    
    def test_example2(self):
        """示例2: 对称结构"""
        heightMap = [[3, 3, 3, 3, 3],
                     [3, 2, 2, 2, 3],
                     [3, 2, 1, 2, 3],
                     [3, 2, 2, 2, 3],
                     [3, 3, 3, 3, 3]]
        expected = 10
        
        self.assertEqual(self.solution.trapRainWater(heightMap), expected)
        self.assertEqual(self.solution_opt.trapRainWater(heightMap), expected)
        # 内存优化版本需要新数组
        heightMap_copy = [[3, 3, 3, 3, 3],
                          [3, 2, 2, 2, 3],
                          [3, 2, 1, 2, 3],
                          [3, 2, 2, 2, 3],
                          [3, 3, 3, 3, 3]]
        self.assertEqual(self.solution_mem.trapRainWater(heightMap_copy), expected)
        self.assertEqual(self.solution_alt.trapRainWater(heightMap), expected)
    
    def test_custom(self):
        """自定义测试"""
        heightMap = [[3, 5, 5, 5, 5],
                     [5, 5, 3, 1, 5],
                     [2, 3, 4, 2, 5],
                     [5, 5, 5, 5, 5]]
        expected = 6
        
        self.assertEqual(self.solution.trapRainWater(heightMap), expected)
        self.assertEqual(self.solution_opt.trapRainWater(heightMap), expected)
        heightMap_copy = [[3, 5, 5, 5, 5],
                          [5, 5, 3, 1, 5],
                          [2, 3, 4, 2, 5],
                          [5, 5, 5, 5, 5]]
        self.assertEqual(self.solution_mem.trapRainWater(heightMap_copy), expected)
        self.assertEqual(self.solution_alt.trapRainWater(heightMap), expected)
    
    def test_edge_cases(self):
        """边界情况 - 仅测试有边界检查的版本"""
        # 空矩阵
        self.assertEqual(self.solution_opt.trapRainWater([]), 0)
        self.assertEqual(self.solution_mem.trapRainWater([]), 0)
        self.assertEqual(self.solution_alt.trapRainWater([]), 0)
        
        # 太小的矩阵
        self.assertEqual(self.solution_opt.trapRainWater([[1, 2]]), 0)
        self.assertEqual(self.solution_mem.trapRainWater([[1, 2]]), 0)
        self.assertEqual(self.solution_alt.trapRainWater([[1, 2]]), 0)
        
        # 全部相同高度
        heightMap = [[5, 5, 5],
                     [5, 5, 5],
                     [5, 5, 5]]
        self.assertEqual(self.solution_opt.trapRainWater(heightMap), 0)
        heightMap_copy = [[5, 5, 5],
                          [5, 5, 5],
                          [5, 5, 5]]
        self.assertEqual(self.solution_mem.trapRainWater(heightMap_copy), 0)
        self.assertEqual(self.solution_alt.trapRainWater(heightMap), 0)
        
        # 最小能存水的矩阵
        heightMap = [[5, 5, 5],
                     [5, 1, 5],
                     [5, 5, 5]]
        expected = 4
        self.assertEqual(self.solution_opt.trapRainWater(heightMap), expected)
        heightMap_copy = [[5, 5, 5],
                          [5, 1, 5],
                          [5, 5, 5]]
        self.assertEqual(self.solution_mem.trapRainWater(heightMap_copy), expected)
        self.assertEqual(self.solution_alt.trapRainWater(heightMap), expected)


# =====================================================================
# 性能对比函数 (可选)
# =====================================================================
def compare_performance():
    """
    对比不同版本的性能
    需要安装 time 模块
    """
    import time
    import copy
    
    # 测试用例
    test_case = [[3, 3, 3, 3, 3] * 40 for _ in range(40)]
    
    solutions = [
        ("原始版本", Solution()),
        ("优化版本", SolutionOptimized()),
        ("内存优化", SolutionMemoryOptimized()),
        ("Set版本", SolutionAlternative()),
    ]
    
    print("\n" + "="*60)
    print("性能对比测试 (200x200 矩阵)")
    print("="*60)
    
    for name, solution in solutions:
        test_data = copy.deepcopy(test_case)
        start = time.time()
        result = solution.trapRainWater(test_data)
        end = time.time()
        print(f"{name:12s}: {(end-start)*1000:6.2f}ms  结果={result}")
    
    print("="*60)


if __name__ == "__main__":
    # 运行测试
    print("\n🧪 运行单元测试...")
    unittest.main(verbosity=2, exit=False)
    
    # 可选：运行性能对比
    # print("\n📊 运行性能对比...")
    # compare_performance()
