# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Each element in dp is a tuple of 3 elements (after i days condition):
        # 1. No stock, not in cool down period
        # 2. No stock, in cool down period
        # 3. Have stock
        n = len(prices)

        dp = [
            (0, 0, 0)
        ] * n

        dp[0] = (0, 0, -prices[0])

        for i in range(1, n):
            dp[i] = (
                max(dp[i-1][1], dp[i-1][0]),
                dp[i-1][2] + prices[i],
                max(dp[i-1][2], dp[i-1][0] - prices[i])
            )

        return max(max(dp[-1]), 0) 
    
if __name__ == "__main__":
    s = Solution()
    prices = [1,2,3,0,2]
    print(s.maxProfit(prices)) # 3