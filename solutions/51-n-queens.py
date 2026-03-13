# https://leetcode.com/problems/n-queens/description/
"""
51. N-Queens (Hard)

Place n queens on an n×n chessboard so that no two queens threaten each other.
Return all distinct solutions, where each solution is a board configuration
represented as a list of strings.

Approach: Backtracking with Column/Diagonal Tracking
- Place queens row by row (one per row is guaranteed).
- Track occupied columns, main diagonals (row - col), and anti-diagonals
  (row + col) using sets for O(1) conflict checking.
- When all n rows are filled, record the board configuration.
- Time: O(n!) — roughly n choices for row 0, n-1 for row 1, etc.
- Space: O(n^2) for the board; O(n) for the tracking sets
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results: list[list[str]] = []
        # Track which columns and diagonals are under attack
        cols: set[int] = set()
        diag: set[int] = set()       # row - col (main diagonal)
        anti_diag: set[int] = set()  # row + col (anti-diagonal)
        board: list[list[str]] = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                # All queens placed — record solution
                results.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue  # skip conflicting positions

                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = '.'
                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return results
