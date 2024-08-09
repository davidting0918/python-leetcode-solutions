# https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09
from typing import List, Tuple
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        Logic: a magic square must have 5 in the center and sum of all rows, columns and diagonals must be 15
        """

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 5:
                    if self.is_magic_square(grid, i, j):
                        result += 1
        return result

    def is_magic_square(self, grid: List[List[int]], i: int, j: int) -> bool:
        # check valid, i and j can't be at the edge
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            return False

        # check 1-9
        if set(grid[i - 1][j - 1:j + 2] + grid[i][j - 1:j + 2] + grid[i + 1][j - 1:j + 2]) != set(range(1, 10)):
            return False

        # sum horizontally
        if sum(grid[i - 1][j - 1:j + 2]) != 15 or sum(grid[i][j - 1:j + 2]) != 15 or sum(grid[i + 1][j - 1:j + 2]) != 15:
            return False

        # sum vertically
        if sum(grid[k][j - 1] for k in range(i - 1, i + 2)) != 15 or sum(grid[k][j] for k in range(i - 1, i + 2)) != 15 or sum(grid[k][j + 1] for k in range(i - 1, i + 2)) != 15:
            return False

        # sum diagonally
        if grid[i - 1][j - 1] + grid[i + 1][j + 1] != 10 or grid[i - 1][j + 1] + grid[i + 1][j - 1] != 10:
            return False

        return True


if __name__ == "__main__":
    s = Solution()

    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    print(s.numMagicSquaresInside(grid))
