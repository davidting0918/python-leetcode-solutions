# https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25
from sys import prefix
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total_sum = sum(grid[i][j] for j in range(n) for i in range(m))\

        if total_sum % 2 == 1:
            return False

        else:
            target = total_sum // 2
        
        row_sum = [sum(grid[i]) for i in range(m)]
        col_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        current = 0
        for i in range(m - 1):
            current += row_sum[i]
            if current == target:
                return True

        current = 0
        for j in range(n - 1):
            current += col_sum[j]
            if current == target:
                return True

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionGrid([[14742,71685,59237,27190]]))
    print(s.canPartitionGrid([[1,3],[2,4]]))
    
