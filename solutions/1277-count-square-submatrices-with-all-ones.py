# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0

        output = [
            [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    output[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    output[i][j] = min(output[i - 1][j], output[i][j - 1], output[i - 1][j - 1]) + 1

                result += output[i][j]
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.countSquares([
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]))