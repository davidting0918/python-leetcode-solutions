# https://leetcode.com/contest/weekly-contest-434/problems/maximum-frequency-after-subarray-operation/?slug=maximum-frequency-after-subarray-operation&region=global_v2
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # find nums == k
        n = len(nums)

        num_count = {
            num: 0 for num in set(nums)
        }
        num_count[k] = 0

        dp = [0] * n
        dp[0] = 1
        num_count[nums[0]] += 1
        for i in range(1, n):
            num_count[nums[i]] += 1
            dp[i] = max(dp[i-1], num_count[nums[i]] + num_count[k])
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    nums = [6, 1, 6]
    k = 1
    print(s.maxFrequency(nums, k))