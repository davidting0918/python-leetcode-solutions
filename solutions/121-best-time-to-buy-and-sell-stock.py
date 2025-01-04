# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5