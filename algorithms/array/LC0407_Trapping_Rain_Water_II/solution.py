"""
LeetCode题目: Trapping Rain Water II
题目编号: 407
难度: 困难
题目链接: https://leetcode.cn/problems/trapping-rain-water-ii/

解题日期: 2025年10月3日
"""

import unittest
import heapq
from typing import List, Optional


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        total_water = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试用例"""
        # 示例1
        heightMap1 = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        self.assertEqual(self.solution.trapRainWater(heightMap1), 4)

        # 示例2
        heightMap2 = [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
        self.assertEqual(self.solution.trapRainWater(heightMap2), 10)

        # 你自己的测试
        heightMap3 = [[3, 5, 5, 5, 5], [5, 5, 3, 1, 5], [2, 3, 4, 2, 5], [5, 5, 5, 5, 5]]
        self.assertEqual(self.solution.trapRainWater(heightMap3), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
