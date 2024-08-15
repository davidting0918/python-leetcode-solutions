# https://leetcode.com/problems/delete-and-earn/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Logic: in each step need to decide whether to delete a number or not, need to decide between
        1. delete current value + points from 2 steps before
        2. points from previous step
        """

        nums.sort()
        values = [0] * (nums[-1] + 1)
        dp = [0] * (nums[-1] + 1)

        for num in set(nums):
            values[num] = nums.count(num) * num

        points = 0
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], dp[i-2] + values[i])
            points = max(points, dp[i])
        return points

if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([2,2,3,3,3,4]))