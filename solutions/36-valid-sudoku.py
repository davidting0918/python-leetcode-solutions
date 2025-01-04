# https://leetcode.com/problems/valid-sudoku/description/
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return


if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))