"""
329. Longest Increasing Path in a Matrix (Hard)
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integers matrix, return the length of the longest increasing path.
From each cell, you can move in four directions (up, down, left, right).
You cannot move diagonally or outside the boundary.

Approach: DFS with Memoization (Top-Down DP)
- For each cell, DFS to all 4 neighbors with strictly greater value.
- Cache the result for each cell to avoid recomputation.
- The strictly increasing constraint guarantees no cycles, so no visited set needed.
- Time: O(m * n) — each cell computed exactly once.
- Space: O(m * n) for the memo table.
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]

            best = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            memo[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(m) for c in range(n))
