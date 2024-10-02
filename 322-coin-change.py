# https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-100-liked
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # 3
