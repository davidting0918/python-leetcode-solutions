# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # logic: found any isolated 1, return -1.
        # 1. use BFS to simulate the rotting process. and since need to calculate the time, so use BFS.

        rows, columns = len(grid), len(grid[0])
        queue = []  # the item format is (row, column, time)
        fresh_count = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # as the starting point of rotting
                if grid[r][c] == 1:
                    fresh_count += 1

        # if queue still have item, means still have fresh orange to rot
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0)  # up
        ]
        minute_output = 0
        while queue:
            row, column, minute = queue.pop(0)
            minute_output = minute

            for dr, dc in directions:
                new_row, new_column = row + dr, column + dc
                if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == 1:
                    grid[new_row][new_column] = 2
                    fresh_count -= 1
                    queue.append((new_row, new_column, minute + 1))

        return -1 if fresh_count > 0 else minute_output


if __name__ == "__main__":
    s = Solution()
    grid = [[0,2]]
    print(s.orangesRotting(grid))