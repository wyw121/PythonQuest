"""
LeetCode题目: Two Sum
题目编号: 1
难度: 简单
题目链接: https://leetcode.cn/problems/two-sum/

解题日期: 2025-09-25
"""

from typing import List, Optional
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解法一：暴力解法
        时间复杂度：O(n²)
        空间复杂度：O(1)

        思路：
        1. 双重循环遍历所有可能的数字对
        2. 检查每对数字的和是否等于target
        3. 找到则返回对应的索引
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:
        """
        解法二：哈希表优化解法
        时间复杂度：O(n)
        空间复杂度：O(n)

        思路：
        1. 使用哈希表存储已遍历的数字及其索引
        2. 对于每个数字，计算complement = target - num
        3. 检查complement是否在哈希表中，如果在则找到答案
        """
        hashmap = {}  # 存储 {数值: 索引}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_examples(self):
        """测试LeetCode给出的示例"""
        # 示例1
        self.assertEqual(self.solution.twoSumOptimized([2, 7, 11, 15], 9), [0, 1])

        # 示例2
        self.assertEqual(self.solution.twoSumOptimized([3, 2, 4], 6), [1, 2])

        # 示例3
        self.assertEqual(self.solution.twoSumOptimized([3, 3], 6), [0, 1])

    def test_edge_cases(self):
        """测试边界情况"""
        # 最小数组长度
        self.assertEqual(self.solution.twoSumOptimized([1, 2], 3), [0, 1])

        # 负数
        self.assertEqual(
            self.solution.twoSumOptimized([-1, -2, -3, -4, -5], -8), [2, 4]
        )

    def test_both_methods(self):
        """测试两种方法结果一致性"""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
        ]

        for nums, target in test_cases:
            result1 = self.solution.twoSum(nums, target)
            result2 = self.solution.twoSumOptimized(nums, target)
            # 验证两种方法找到的索引对应的数字和都等于target
            self.assertEqual(nums[result1[0]] + nums[result1[1]], target)
            self.assertEqual(nums[result2[0]] + nums[result2[1]], target)


if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)
