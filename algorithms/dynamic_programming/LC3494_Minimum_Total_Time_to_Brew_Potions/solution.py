"""
LeetCode题目: Minimum Total Time to Brew Potions
题目编号: 3494
难度: 中等
题目链接: https://leetcode.cn/problems/minimum-total-time-to-brew-potions/

解题日期: 2025年10月9日
"""

import unittest
from typing import List, Optional


class Solution:
    def minimumTime(self, skill: List[int], mana: List[int]) -> int:
        # ==================== 错误代码（已注释）====================
        # m, n = len(mana), len(skill)
        # finish_table = [[0] * m for _ in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         if i == 0 or j == 0:
        #             finish_table[i][j] = skill[i] * mana[j]
        #             # ❌ 错误1: 第一行和第一列应该是累加的，不是单独计算
        #             # 例如: finish_table[0][1] 应该是 finish_table[0][0] + skill[0] * mana[1]
        #             # 而不是直接 skill[0] * mana[1]
        #
        #         if finish_table[i - 1][j] and finish_table[i][j - 1]:
        #             finish_table[i][j] = (
        #                 max(finish_table[i - 1][j], finish_table[i][j - 1])
        #                 + skill[i] * mana[j]
        #             )
        #             # ❌ 错误2: 这个条件判断有问题
        #             # - 当 i=0 或 j=0 时，i-1 或 j-1 会越界
        #             # - and 条件意味着两个都非零才执行，逻辑不对
        #             # - 这个 if 和上面的 if 可能都会执行，导致覆盖
        #
        # return finish_table[n - 1][m - 1]
        # =========================================================

        # ==================== 正确解法（请在此补充）====================
        # 思路提示:
        # 1. 创建 finish_table，大小为 n*m
        # 2. 初始化第一个格子 (0,0)
        # 3. 初始化第一行（巫师0处理所有药水，累加）
        # 4. 初始化第一列（所有巫师处理药水0，累加）
        # 5. 填充其他格子: max(左边, 上面) + 当前处理时间
        # 6. 返回右下角的值
        # ============================================================

        # ==================== 第二次尝试（已注释）====================
        # m, n = len(mana), len(skill)
        # finish = [[0] * m for _ in range(n)]
        # finish[0][0] = skill[0] * mana[0]
        #
        # for j in range(1, m):
        #     finish[0][j] = finish[0][j - 1] + skill[0] * mana[j]
        #
        # for i in range(1, n):
        #     finish[i][0] = finish[i - 1][0] + skill[i] * mana[0]
        #
        # for i in range(1, n):
        #     for j in range(1, m):
        #         finish[i][j] = (
        #             max(finish[i - 1][j], finish[i][j - 1]) + skill[i] * mana[j]
        #         )
        # return finish[n - 1][m - 1]
        #
        # ❌ 这个思路的问题：
        # 理解错了题意！题目不是简单的"流水线累加"问题
        #
        # 错误理解：以为每个药水必须紧接着上一个药水开始
        # 实际情况：每个药水可以"延迟"开始，以避免后面的巫师"堵车"
        #
        # 示例1中，药水1不是在时间0开始，而是在时间52开始！
        # 这样做是为了让所有巫师都能高效工作，避免等待
        # =========================================================

        # ==================== 正确解法（请在此补充）====================
        # 重新理解题意：
        # 这道题的核心是找到每个药水的"最佳开始时间"
        #
        # 关键点：
        # 1. finish[i][j] = 巫师i完成药水j的时间
        # 2. 巫师i开始处理药水j的时间 = max(两个条件)
        #    - 条件1: 巫师i处理完药水j-1（自己空闲）
        #    - 条件2: 巫师i-1处理完药水j（药水传过来）
        # 3. 但这里有个问题：药水j的"开始时间"可以调整！
        #
        # 思路提示：
        # 需要考虑药水之间的"错峰"启动策略
        # 具体算法待补充...
        # ============================================================

        m, n = len(skill), len(mana)
        finish = [[0] * n for _ in range(m)]
        start = [[0] * n for _ in range(m)]
        finish[0][0] = skill[0] * mana[0]

        for j in range(1, n):
            start[0][j] = finish[0][j - 1]
            finish[0][j] = start[0][j] + skill[0] * mana[j]

        for i in range(1, n):
            start[i][0] = max(
                finish[i - 1][0],
            )
            finish[i][0] = finish[i - 1][0] + skill[i] * mana[0]
        #
        # for i in range(1, n):
        #     for j in range(1, m):
        #         finish[i][j] = (
        #             max(finish[i - 1][j], finish[i][j - 1]) + skill[i] * mana[j]
        #         )
        # return finish[n - 1][m - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例1"""
        skill = [1, 5, 2, 4]
        mana = [5, 1, 4, 2]
        result = self.solution.minimumTime(skill, mana)
        print(f"\n测试用例1: skill={skill}, mana={mana}")
        print(f"输出结果: {result}")
        print(f"预期结果: 110")
        self.assertEqual(result, 110)

    def test_example2(self):
        """测试示例2"""
        skill = [1, 1, 1]
        mana = [1, 1, 1]
        result = self.solution.minimumTime(skill, mana)
        print(f"\n测试用例2: skill={skill}, mana={mana}")
        print(f"输出结果: {result}")
        print(f"预期结果: 5")
        self.assertEqual(result, 5)

    def test_example3(self):
        """测试示例3"""
        skill = [1, 2, 3, 4]
        mana = [1, 2]
        result = self.solution.minimumTime(skill, mana)
        print(f"\n测试用例3: skill={skill}, mana={mana}")
        print(f"输出结果: {result}")
        print(f"预期结果: 21")
        self.assertEqual(result, 21)


if __name__ == "__main__":
    unittest.main(verbosity=2)
