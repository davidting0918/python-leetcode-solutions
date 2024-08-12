# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i-1])
            dp[i] = max(dp[i-1], prices[i] - min_price)
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5