# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        for i in range(n):

            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices

if __name__ == "__main__":
    s = Solution()
    prices = [8,4,6,2,3]
    print(s.finalPrices(prices)) # [4,2,4,2,3]