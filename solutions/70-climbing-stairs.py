# https://leetcode.com/problems/climbing-stairs/description/
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Logic: if want to climb on step n, can either climb from step n-1 or n-2.
        so the total step: step_n = step_n-1 + step_n-2
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n

        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2)) # 2
    print(s.climbStairs(3)) # 3