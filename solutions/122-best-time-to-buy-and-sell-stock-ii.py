# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Find all the ascending subarray and sum the difference
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit


if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))

    prices = [1,2,3,4,5]
    print(s.maxProfit(prices))

    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))