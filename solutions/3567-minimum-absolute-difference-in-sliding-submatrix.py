from math import inf
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        answer = [
            [0] * (n - k + 1) for _ in range(m - k + 1)
        ]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = sorted(set(
                    grid[x][y] for x in range(i, i + k) for y in range(j, j + k)
                ))

                if len(nums) <= 1:
                    continue

                min_diff = float('inf')
                for z in range(len(nums) - 1):
                    diff = nums[z + 1] - nums[z]
                    if diff < min_diff:
                        min_diff = diff
                    if min_diff == 1:
                        break

                answer[i][j] = min_diff

        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.minAbsDiff([[1,8],[3,-2]], 2))
    print(s.minAbsDiff([[1,-2,3],[2,3,5]], 2))
    print(s.minAbsDiff([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]], 5))