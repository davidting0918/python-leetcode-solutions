# https://leetcode.com/problems/unique-paths-ii/description/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        grids = [
            [0 for _ in range(len(obstacleGrid[0]))]
            for _ in range(len(obstacleGrid))
        ]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    grids[i][j] = 0
                elif i == 0 and j == 0:
                    grids[i][j] = 1
                elif i == 0:
                    grids[i][j] = grids[i][j - 1]
                elif j == 0:
                    grids[i][j] = grids[i - 1][j]
                else:
                    grids[i][j] = grids[i - 1][j] + grids[i][j - 1]
        return grids[-1][-1]


if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    
    print(s.uniquePathsWithObstacles(obstacleGrid))
    
    obstacleGrid = [[0,1],[1,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))