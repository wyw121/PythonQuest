"""
LeetCode题目: Triangle
题目编号: 120
难度: 中等
题目链接: https://leetcode.cn/problems/triangle/

解题日期: 2025-09-25
"""

import unittest
from typing import List, Optional


class Solution:

    def minimumTotal(self, triangle):
        a = len(triangle)
        for i in range(a - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试用例"""
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
