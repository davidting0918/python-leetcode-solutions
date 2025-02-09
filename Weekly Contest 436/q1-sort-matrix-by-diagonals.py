# https://leetcode.com/contest/weekly-contest-436/problems/sort-matrix-by-diagonals/description/

from typing import List
from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # 1. Collect diagonals
        diagonals1 = defaultdict(list)
        diagonals2 = defaultdict(list)

        for r in range(n):
            for c in range(n):
                if r >= c:
                    diagonals1[r - c].append(grid[r][c])
                else:
                    diagonals2[r - c].append(grid[r][c])

        # 2. Sort diagonals
        for key in diagonals1:
            diagonals1[key].sort(reverse=True)  # descending order
        for key in diagonals2:
            diagonals2[key].sort()  # ascending order

        # 3. Refill grid
        for r in range(n):
            for c in range(n):
                if r >= c:
                    grid[r][c] = diagonals1[r - c].pop(0)
                else:
                    grid[r][c] = diagonals2[r - c].pop(0)

        return grid


if __name__ == '__main__':
    s = Solution()
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    print(s.sortMatrix(grid))
