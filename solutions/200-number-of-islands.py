# https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-100-liked
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Logic: if reach land, label all the land attached to it as 0. to ensure if reach a "1" in the main loop,
        # it is a new island. This is a DFS approach.

        def dfs(r: int, c: int):

            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        rows = len(grid)
        columns = len(grid[0])

        land_count = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    dfs(row, column)
                    land_count += 1

        return land_count


if __name__ == "__main__":
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid)) # 1