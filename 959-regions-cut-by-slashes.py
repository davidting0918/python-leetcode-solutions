# https://leetcode.com/problems/regions-cut-by-slashes/description/?envType=daily-question&envId=2024-08-10
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(x: int, y: int):
            if x < 0 or x >= 3 * len(grid) or y < 0 or y >= 3 * len(grid) or graphs[x][y] != 0:
                return

            graphs[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        ht = {
            "/": [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
            "\\": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            " ": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        }

        graphs = []
        for i in range(len(grid) * 3):
            graphs.append([])

        for i in range(len(grid)):
            for k in grid[i]:
                graphs[3 * i] += ht[k][0]
                graphs[3 * i + 1] += ht[k][1]
                graphs[3 * i + 2] += ht[k][2]

        results = 0
        for i in range(3 * len(grid)):
            for j in range(3 * len(grid)):
                if graphs[i][j] == 0:
                    print(f"Found a region at {i}, {j}")
                    dfs(i, j)
                    results += 1

        return results


if __name__ == "__main__":
    s = Solution()
    grid = [" /", "/ "]
    print(s.regionsBySlashes(grid))

    grid = ["//","/ "]
    print(s.regionsBySlashes(grid))