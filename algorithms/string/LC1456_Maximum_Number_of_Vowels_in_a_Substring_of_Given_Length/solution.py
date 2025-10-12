"""
LeetCode题目: Maximum Number of Vowels in a Substring of Given Length
题目编号: 1456
难度: 中等
题目链接: https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

解题日期: 2025年10月12日
"""

import unittest
from typing import List, Optional


class Solution:
    # ========== 方法1: 暴力法（你的原始解法）==========
    def maxVowels(self, s: str, k: int) -> int:
        """
        暴力法: 遍历每个窗口，重新计算元音数量
        时间复杂度: O(n * k)
        空间复杂度: O(1)
        """
        a = ["a", "e", "i", "o", "u"]
        n = len(s)
        count = 0
        max_count = 0  # 避免覆盖内置函数max
        for i in range(0, n - k + 1):
            for j in range(k):
                if s[i + j] in a:
                    count += 1
            max_count = max(max_count, count)
            count = 0
        return max_count

    # ========== 方法2: 滑动窗口（优化版）==========
    def maxVowels_sliding_window(self, s: str, k: int) -> int:
        """
        滑动窗口法: 只在窗口边界更新时调整计数
        时间复杂度: O(n)
        空间复杂度: O(1)
        特别优化: 当找到k个元音时提前退出
        """

        def impact_of(char: str) -> int:
            """返回该字符的元音贡献值: 元音返回1，非元音返回0"""
            return 1 if char in "aeiou" else 0

        # 步骤1: 初始化第一个窗口
        window_value = result = 0
        for i in range(k):
            window_value += impact_of(s[i])
        result = window_value

        # 步骤2: 滑动窗口
        for i in range(k, len(s)):
            window_value -= impact_of(s[i - k])  # 移除左边元素
            window_value += impact_of(s[i])  # 添加右边元素
            result = max(window_value, result)
            if result == k:  # 提前退出优化：已达到最大可能值
                return k

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 测试方法1: 暴力法
    def test_example1_brute_force(self):
        """测试用例1 (暴力法): s = "abciiidef", k = 3"""
        result = self.solution.maxVowels("abciiidef", 3)
        self.assertEqual(result, 3)

    def test_example2_brute_force(self):
        """测试用例2 (暴力法): s = "aeiou", k = 2"""
        result = self.solution.maxVowels("aeiou", 2)
        self.assertEqual(result, 2)

    def test_example3_brute_force(self):
        """测试用例3 (暴力法): s = "leetcode", k = 3"""
        result = self.solution.maxVowels("leetcode", 3)
        self.assertEqual(result, 2)

    def test_example4_brute_force(self):
        """测试用例4 (暴力法): s = "rhythms", k = 4"""
        result = self.solution.maxVowels("rhythms", 4)
        self.assertEqual(result, 0)

    def test_example5_brute_force(self):
        """测试用例5 (暴力法): s = "tryhard", k = 4"""
        result = self.solution.maxVowels("tryhard", 4)
        self.assertEqual(result, 1)

    # 测试方法2: 滑动窗口
    def test_example1_sliding_window(self):
        """测试用例1 (滑动窗口): s = "abciiidef", k = 3"""
        result = self.solution.maxVowels_sliding_window("abciiidef", 3)
        self.assertEqual(result, 3)

    def test_example2_sliding_window(self):
        """测试用例2 (滑动窗口): s = "aeiou", k = 2"""
        result = self.solution.maxVowels_sliding_window("aeiou", 2)
        self.assertEqual(result, 2)

    def test_example3_sliding_window(self):
        """测试用例3 (滑动窗口): s = "leetcode", k = 3"""
        result = self.solution.maxVowels_sliding_window("leetcode", 3)
        self.assertEqual(result, 2)

    def test_example4_sliding_window(self):
        """测试用例4 (滑动窗口): s = "rhythms", k = 4"""
        result = self.solution.maxVowels_sliding_window("rhythms", 4)
        self.assertEqual(result, 0)

    def test_example5_sliding_window(self):
        """测试用例5 (滑动窗口): s = "tryhard", k = 4"""
        result = self.solution.maxVowels_sliding_window("tryhard", 4)
        self.assertEqual(result, 1)

    # 对比测试: 确保两种方法结果一致
    def test_compare_methods(self):
        """对比两种方法的结果是否一致"""
        test_cases = [
            ("abciiidef", 3, 3),
            ("aeiou", 2, 2),
            ("leetcode", 3, 2),
            ("rhythms", 4, 0),
            ("tryhard", 4, 1),
        ]
        for s, k, expected in test_cases:
            result1 = self.solution.maxVowels(s, k)
            result2 = self.solution.maxVowels_sliding_window(s, k)
            self.assertEqual(result1, expected, f"暴力法失败: {s}, {k}")
            self.assertEqual(result2, expected, f"滑动窗口失败: {s}, {k}")
            self.assertEqual(result1, result2, f"两种方法结果不一致: {s}, {k}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
