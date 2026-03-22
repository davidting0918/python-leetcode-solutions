from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)
        r0 = r1 = r2 = r3 = True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    r0 = False
                if mat[i][j] != target[j][n - 1 - i]:
                    r1 = False
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    r2 = False
                if mat[i][j] != target[n - 1 - j][i]:
                    r3 = False

        return r0 or r1 or r2 or r3

if __name__ == "__main__":
    s = Solution()
    print(s.findRotation([[0,1],[1,0]], [[1,0],[0,1]]))
    print(s.findRotation([[0,1],[1,1]], [[1,0],[0,1]]))
    print(s.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))

