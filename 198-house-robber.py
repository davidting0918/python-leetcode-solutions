# https://leetcode.com/problems/house-robber/description/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Logic: in each house, need to get the max amount between
        (rob current house + amount robbed from 2 houses before) and (amount robbed from previous house),
        which one is greater is the best amount to rob the current house.
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i < 2:
                dp[i] = max(nums[:i+1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [2,1,1,2]
    print(s.rob(nums))