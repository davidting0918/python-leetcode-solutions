from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        

        for col in range(y, y + k):

            start_row = x
            for turn in range(k // 2):
                grid[start_row + turn][col], grid[start_row + k - turn - 1][col] = grid[start_row + k - turn - 1][col], grid[start_row + turn][col]           
        return grid

if __name__ == '__main__':
    s = Solution()
    print(s.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3))
    print(s.reverseSubmatrix([[14,3,18,16],[2,14,11,20],[19,19,4,15],[11,15,18,6]], 0, 0, 4))
