# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Logic: need to climb at len(cost) + 1 steps, so create a dp array of len(cost) + 1.
        level n can reach from level n-1 or n-2, so the cost to reach level n is the minimum cost between 
        (cost to reach level n-1 + cost of level n-1) and (cost to reach level n-2 + cost of level n-2)
        """
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20])) # 15
