# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/?envType=daily-question&envId=2025-01-18
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # since there are only 2 rows, so just need to decide when the first robot need to move to the second row.
        # use the prefix sum of the 2 rows to solve this problem
        rows = 2
        cols = len(grid[0])

        prefix1 = [0] * (cols + 1)
        prefix2 = [0] * (cols + 1)

        for i in range(cols):
            prefix1[i + 1] = prefix1[i] + grid[0][i]
            prefix2[i + 1] = prefix2[i] + grid[1][i]
        return

if __name__ == "__main__":
    s = Solution()
    grid = [[2,5,4],[1,5,1]]
    print(s.gridGame(grid))
