# https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Logic: From bottom to top, each cell has 3 choices, can add the min between (x-1, x, x+1) from the bottom row except for the last row. 
        """
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for y in range(n-1, -1, -1):
            for x in range(n):
                if y == n-1:
                    dp[y][x] = matrix[y][x]
                else:
                    if x == 0:
                        dp[y][x] = matrix[y][x] + min(dp[y+1][x], dp[y+1][x+1])
                    elif x == n-1:
                        dp[y][x] = matrix[y][x] + min(dp[y+1][x-1], dp[y+1][x])
                    else:
                        dp[y][x] = matrix[y][x] + min(dp[y+1][x-1], dp[y+1][x], dp[y+1][x+1])
                continue
        return min(dp[0])

if __name__ == "__main__":
    s = Solution()
    print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))


