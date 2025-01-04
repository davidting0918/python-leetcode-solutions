# https://leetcode.com/problems/stone-game-ii/description/?envType=daily-question&envId=2024-08-20
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        This solution copy the logic from:
        https://leetcode.com/problems/stone-game-ii/solutions/5662713/98-55-easy-solution-with-explanation/?envType=daily-question&envId=2024-08-20
        """
        suffix_sum = [
            sum(piles[i:]) for i in range(len(piles))
        ]
        n = len(piles)

        dp = [[0]*(n+1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(
                            dp[i][m],
                            suffix_sum[i] - dp[i+x][max(m, x)]
                        )
        return dp[0][1]
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGameII([2,7,9,4,4]))