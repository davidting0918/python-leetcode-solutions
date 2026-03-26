# https://leetcode.com/problems/equal-sum-grid-partition-ii/?envType=daily-question&envId=2026-03-26
from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] for i in range(m) for j in range(n))

        if self._try_row_cuts(grid, m, n, total):
            return True

        grid_t = [[grid[i][j] for i in range(m)] for j in range(n)]
        if self._try_row_cuts(grid_t, n, m, total):
            return True

        return False

    def _try_row_cuts(self, grid, m, n, total):
        if m < 2:
            return False

        top_counter = Counter()
        bottom_counter = Counter()

        for row in grid:
            for v in row:
                bottom_counter[v] += 1

        top_sum = 0
        for i in range(m - 1):
            for j in range(n):
                v = grid[i][j]
                top_counter[v] += 1
                bottom_counter[v] -= 1
                if bottom_counter[v] == 0:
                    del bottom_counter[v]

            top_sum += sum(grid[i])
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = top_sum - bottom_sum
            target = abs(diff)

            if diff > 0:
                if self._can_remove(target, top_counter, grid, 0, i, n, i + 1):
                    return True
            else:
                if self._can_remove(target, bottom_counter, grid, i + 1, m - 1, n, m - 1 - i):
                    return True

        return False

    def _can_remove(self, target, counter, grid, row_start, row_end, n, num_rows):
        if num_rows >= 2 and n >= 2:
            return counter.get(target, 0) > 0

        if num_rows == 1 and n == 1:
            return False

        if num_rows == 1:
            return grid[row_start][0] == target or grid[row_start][n - 1] == target

        if n == 1:
            return grid[row_start][0] == target or grid[row_end][0] == target

        return False

if __name__ == '__main__':
    s = Solution()

    # Example 1
    assert s.canPartitionGrid([[1,4],[2,3]]) == True
    # Example 2
    assert s.canPartitionGrid([[1,2],[3,4]]) == True
    # Example 3
    assert s.canPartitionGrid([[1,2,4],[2,3,5]]) == False
    # Example 4
    assert s.canPartitionGrid([[4,1,8],[3,2,6]]) == False

    print("All test cases passed!")
