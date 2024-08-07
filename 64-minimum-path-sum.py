# https://leetcode.com/problems/minimum-path-sum/description/
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Logic: each cell can only reach from the top or left cell, and calculated the minimum cost to the current cell
        """

        grids = [
            [0 for _ in range(len(grid[0]))]
            for _ in range(len(grid))
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grids[i][j] = grid[i][j]
                elif i == 0:
                    grids[i][j] = grids[i][j - 1] + grid[i][j]
                elif j == 0:
                    grids[i][j] = grids[i - 1][j] + grid[i][j]
                else:
                    grids[i][j] = min(grids[i - 1][j], grids[i][j - 1]) + grid[i][j]

        return grids[-1][-1]


if __name__ == "__main__":
    s = Solution()
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(s.minPathSum(grid))
