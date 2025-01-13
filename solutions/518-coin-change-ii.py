# https://leetcode.com/problems/coin-change-ii/description/?envType=study-plan-v2&envId=dynamic-programming

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 解題邏輯：每個位置代表組成這個 index 的組合數量
        # 1. 初始化 dp[0] = 1，因為組成 0 的組合只有一種，就是不選
        # 2. 假設先拿 coin = 1, 那每個位置都是 1, 因為每種金額都可以全部用 1 來組成。
        # 3.1 假設第二個 coin = 2, dp[2] += dp[0], 代表組成 2 的組合數量等於組成 2 - 2 的組合數量 + 組成 2 的組合數量,
        # 3.2 dp[4] += dp[2], 代表組成 4 的組合數量等於組成 4 - 2 的組合數量 + 組成 4 的組合數

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

if __name__ == "__main__":
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(s.change(amount, coins)) # 4