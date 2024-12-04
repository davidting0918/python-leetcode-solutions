# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [
            [0 for i in range(len(matrix[0]))] for j in range(len(matrix))
        ]


        for column in range(len(matrix[0])):
            for row in range(len(matrix)):
                if column == 0 or row == 0:
                    dp[row][column] = int(matrix[row][column])
                elif matrix[row][column] == "1":
                    dp[row][column] = min(
                        dp[row-1][column],
                        dp[row][column-1],
                        dp[row-1][column-1]
                    ) + 1
        return max(max(row) for row in dp) ** 2

if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))