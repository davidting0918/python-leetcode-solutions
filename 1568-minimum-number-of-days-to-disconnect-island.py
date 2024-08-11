# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/?envType=daily-question&envId=2024-08-11
from typing import List
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        The answer must be in [0, 1, 2], if original grid has 0 or 2 islands, return 0
        use dfs to visit each cell to calculate the island number
        """
        grid_copy = [row[:] for row in grid]
        num_islands = self.count_islands(grid_copy)

        if num_islands > 1 or num_islands == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid_copy = [row[:] for row in grid]
                    grid_copy[i][j] = 0
                    num_islands = self.count_islands(grid_copy)
                    if num_islands > 1 or num_islands == 0:
                        return 1
        return 2

    def count_islands(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return

            grid[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        island_num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    island_num += 1
        return island_num


if __name__ == "__main__":
    s = Solution()
    # grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    # print(s.minDays(grid))
    #
    # grid = [[1,1]]
    # print(s.minDays(grid))

    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
    print(s.minDays(grid))