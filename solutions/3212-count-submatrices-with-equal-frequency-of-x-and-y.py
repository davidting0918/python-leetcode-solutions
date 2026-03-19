from sre_parse import GROUPREF_IGNORE
from typing import List

class Solution:
    def is_x(self, val):
        return True if val == 'X' else False
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        row, col = len(grid), len(grid[0])

        str_map = {
            "X": 1,
            "Y": -1,
            ".": 0
        }
        has_x = [
            [False for _ in range(col)] for _ in range(row)
        ]

        answer = 0
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    has_x[i][j] = self.is_x(grid[i][j])
                    grid[i][j] = str_map[grid[i][j]]
                elif i == 0:
                    has_x[i][j] = has_x[i][j - 1] or self.is_x(grid[i][j])
                    grid[i][j] = grid[i][j - 1] + str_map[grid[i][j]]
                elif j == 0:
                    has_x[i][j] = has_x[i - 1][j] or self.is_x(grid[i][j])
                    grid[i][j] = grid[i - 1][j] + str_map[grid[i][j]]
                else:
                    has_x[i][j] = has_x[i - 1][j] or has_x[i][j - 1] or has_x[i - 1][j - 1] or self.is_x(grid[i][j])
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1] + str_map[grid[i][j]]
            
                if grid[i][j] == 0 and has_x[i][j]:
                    answer += 1

        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))
    print(s.numberOfSubmatrices([["X","X"],["X","Y"]]))
    print(s.numberOfSubmatrices([[".","."],[".","."]]))