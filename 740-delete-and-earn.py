# https://leetcode.com/problems/delete-and-earn/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Logic: in each step need to decide whether to delete a number or not, need to decide between
        1. delete current value + points from 2 steps before
        2. points from previous step
        """

        max_num = max(nums)
        dp = [0] * (max_num + 1)

        for num in nums:
            dp[num] += num  # like the house robber problem, store the points in the dp array, and if you delete one value you will delete all

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        
        return dp[-1]
                
if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([2,2,3,3,3,4]))