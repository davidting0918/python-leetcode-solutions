# https://leetcode.com/problems/count-sub-islands/description/?envType=daily-question&envId=2024-08-28
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def _recursive(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] == 0:
                return True
            
            if grid1[x][y] == 0:
                res = False
            
            grid2[x][y] = 0

            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                res &= _recursive(i, j)
            return res

        result = 0
        m = len(grid1)
        n = len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and _recursive(i, j):
                    result += 1
        return result
    
if __name__ == "__main__":
    s = Solution()
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

    print(s.countSubIslands(grid1, grid2))
