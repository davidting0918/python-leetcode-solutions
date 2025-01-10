# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/?envType=study-plan-v2&envId=dynamic-programming
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # let transaction fee happen when selling
        # each element in dp is a tuple of 3 elements (after i days condition):
        # 1. hold a stock
        # 2. no stock

        n = len(prices)
        dp = [
            (0, 0)
        ] * n

        dp[0] = (-prices[0], 0)


        for i in range(1, n):
            dp[i] = (
                max(dp[i-1][0], dp[i-1][1] - prices[i]),
                max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
            )
        return max(dp[-1])

if __name__ == '__main__':
    s = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(s.maxProfit(prices, fee))