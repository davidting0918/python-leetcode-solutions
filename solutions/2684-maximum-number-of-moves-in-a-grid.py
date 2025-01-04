# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/?envType=daily-question&envId=2024-10-29
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        output = [
            [0 for _ in grid[0]] for _ in grid
        ]
        deltas = [
            (1, 1),
            (0, 1),
            (-1, 1)
        ]
        m = len(grid)
        n = len(grid[0])

        for col in range(-1, -len(grid[0]) - 1, -1):
            for row in range(-1, -len(grid) - 1, -1):
                if col == -1:
                    output[row][col] = 1
                else:
                    if row == -1:
                        c_deltas = deltas[1:]
                    elif abs(row) == m:
                        c_deltas = deltas[:2]
                    else:
                        c_deltas = deltas

                    for delta in c_deltas:
                        new_row = row + delta[0]
                        new_col = col + delta[1]

                        if grid[new_row][new_col] > grid[row][col]:
                            output[row][col] = max(output[row][col], output[new_row][new_col] + 1)
                        else:
                            output[row][col] = max(output[row][col], 1)

        return max([i[0] for i in output]) - 1


if __name__ == "__main__":
    s = Solution()
    grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
    print(s.maxMoves(grid))