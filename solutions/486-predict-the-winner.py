# https://leetcode.com/problems/predict-the-winner/description/
from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
                # print(f"length: {length}, i: {i}, j: {j}")
                # print(dp)
        return dp[0][n - 1] >= 0


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 2, 7, 8, 4]
    print(nums)
    print(s.predictTheWinner(nums))