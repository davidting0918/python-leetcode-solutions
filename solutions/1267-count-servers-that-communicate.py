# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # count all isolated servers
        answer = 0
        n = len(grid)
        m = len(grid[0])

        rows = [
            sum(grid[i])
            for i in range(n)
        ]

        cols = [
            sum(grid[i][j] for i in range(n))
            for j in range(m)
        ]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    answer += 1
        return answer

if __name__ == "__main__":
    s = Solution()
    grid = [[1, 0, 1], [0, 0, 0], [0, 0, 1]]
    print(s.countServers(grid)) # 0