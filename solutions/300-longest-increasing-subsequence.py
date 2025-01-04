# https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4