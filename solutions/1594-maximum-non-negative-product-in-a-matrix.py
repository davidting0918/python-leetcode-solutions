from re import L
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]  # (max, min) for now
        for i in range(m):
            for j in range(n):
                current_value = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = (current_value, current_value)
                    continue
                elif i == 0:
                    nums = [dp[i][j - 1][0], dp[i][j - 1][1]]
                elif j == 0:
                    nums = [dp[i - 1][j][0], dp[i - 1][j][1]]
                else:
                    nums = [dp[i][j-1][0], dp[i][j-1][1], dp[i-1][j][0], dp[i-1][j][1]]
                
                dp[i][j] = (
                    max(i * current_value for i in nums),
                    min(i * current_value for i in nums)
                )

        MOD = 10**9 + 7
        result = dp[m-1][n-1][0]
        return result % MOD if result >= 0 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
    print(s.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]))