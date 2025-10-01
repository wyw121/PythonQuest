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
    # 方法1: 模拟法（迭代循环）- 你的原方案
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        时间复杂度: O(log n) - 每次兑换使得瓶数减少
        空间复杂度: O(1)
        思路: 循环模拟兑换过程
        """
        total = numBottles
        numEmpty = numBottles
        while numEmpty >= numExchange:
            newBottles = numEmpty // numExchange  # 本轮兑换得到的新瓶数
            total += newBottles
            numEmpty = numEmpty % numExchange + newBottles  # 剩余空瓶 + 新瓶喝完的空瓶
        return total
    
    # 方法2: 数学公式法（最优解）
    def numWaterBottles_math(self, numBottles: int, numExchange: int) -> int:
        """
        时间复杂度: O(1)
        空间复杂度: O(1)
        思路: 推导数学公式，每次兑换本质上是 numExchange-1 个空瓶换 1 瓶水
        
        分析:
        - 初始有 numBottles 瓶水，全部喝完后有 numBottles 个空瓶
        - 每兑换一次，numExchange 个空瓶 -> 1 瓶水（喝完又是1个空瓶）
        - 每次兑换净消耗 numExchange-1 个空瓶，换来1瓶可喝的水
        
        为什么是 (numBottles - 1)？
        - 兑换过程最后一定会剩下至少1个无法兑换的空瓶
        - 可用于兑换的空瓶数 = numBottles - 1
        - 每次净消耗 = numExchange - 1
        - 兑换次数 = (numBottles - 1) / (numExchange - 1)
        
        例: numBottles=4, numExchange=3
        - 4个空瓶 -> 3个兑换1瓶(剩2个) -> 无法继续 = 兑换1次
        - (4-1)/(3-1) = 3/2 = 1 ✓
        """
        if numBottles < numExchange:
            return numBottles
        return numBottles + (numBottles - 1) // (numExchange - 1)
    
    # 方法3: 递归法
    def numWaterBottles_recursive(self, numBottles: int, numExchange: int) -> int:
        """
        时间复杂度: O(log n)
        空间复杂度: O(log n) - 递归栈空间
        思路: 递归计算每一轮兑换
        """
        def helper(empty_bottles):
            if empty_bottles < numExchange:
                return 0
            new_bottles = empty_bottles // numExchange
            remaining = empty_bottles % numExchange
            return new_bottles + helper(new_bottles + remaining)
        
        return numBottles + helper(numBottles)
    
    # 方法4: 优化模拟法（简化版本）
    def numWaterBottles_optimized(self, numBottles: int, numExchange: int) -> int:
        """
        时间复杂度: O(log n)
        空间复杂度: O(1)
        思路: 简化循环逻辑，边喝边兑换
        """
        total = 0
        empty = 0
        
        while numBottles > 0:
            total += numBottles  # 喝掉所有满瓶
            empty += numBottles  # 增加空瓶数
            numBottles = empty // numExchange  # 能兑换的新瓶数
            empty = empty % numExchange  # 剩余空瓶
        
        return total


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试所有方法的基本用例"""
        test_cases = [
            (9, 3, 13),   # 示例1
            (15, 4, 19),  # 示例2
            (1, 3, 1),    # 边界: 无法兑换
            (2, 2, 3),    # 边界: 刚好能兑换一次
        ]
        
        for numBottles, numExchange, expected in test_cases:
            with self.subTest(numBottles=numBottles, numExchange=numExchange):
                self.assertEqual(self.solution.numWaterBottles(numBottles, numExchange), expected)
                self.assertEqual(self.solution.numWaterBottles_math(numBottles, numExchange), expected)
                self.assertEqual(self.solution.numWaterBottles_recursive(numBottles, numExchange), expected)
                self.assertEqual(self.solution.numWaterBottles_optimized(numBottles, numExchange), expected)
    
    def test_edge_cases(self):
        """测试边界情况"""
        # 最小值
        self.assertEqual(self.solution.numWaterBottles_math(1, 2), 1)
        
        # 大量瓶数
        self.assertEqual(self.solution.numWaterBottles_math(100, 3), 149)
        
        # numExchange 很大
        self.assertEqual(self.solution.numWaterBottles_math(5, 10), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
