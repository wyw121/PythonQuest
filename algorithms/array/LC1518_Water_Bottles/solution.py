"""
LeetCode题目: Water Bottles
题目编号: 1518
难度: 简单
题目链接: https://leetcode.cn/problems/water-bottles/

解题日期: 2025年10月1日
"""

import unittest
from typing import List, Optional


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        numEmpty = numBottles
        while numEmpty >= numExchange:
            newBottles = numEmpty // numExchange  # 本轮兑换得到的新瓶数
            total += newBottles
            numEmpty = numEmpty % numExchange + newBottles  # 剩余空瓶 + 新瓶喝完的空瓶
        return total


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试用例"""
        # 示例1: numBottles = 9, numExchange = 3, 输出: 13
        self.assertEqual(self.solution.numWaterBottles(9, 3), 13)

        # 示例2: numBottles = 15, numExchange = 4, 输出: 19
        self.assertEqual(self.solution.numWaterBottles(15, 4), 19)

        # 边界情况: 无法兑换
        self.assertEqual(self.solution.numWaterBottles(1, 3), 1)

        # 边界情况: 刚好能兑换一次
        self.assertEqual(self.solution.numWaterBottles(2, 2), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
