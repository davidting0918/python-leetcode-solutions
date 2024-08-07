# https://leetcode.com/problems/unique-paths-ii/description/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        o_m = 0
        o_n = 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    o_m = i + 1
                    o_n = j + 1
                    break
        
        if o_m == 0 and o_n == 0:
            return self._get_combination(m, n)
        
        print(f"m: {m}, n: {n}, o_m: {o_m}, o_n: {o_n}")
        return self._get_combination(m, n) - (self._get_combination(o_m, o_n) * self._get_combination(m - o_m + 1, n - o_n + 1))
    
    def _get_combination(self, m: int, n: int) -> int:
        total = m + n - 2
        lower = min(m, n) - 1
        result = 1
        for i in range(lower):
            result *= total - i
            result /= i + 1
        return int(result)
        
if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    
    print(s.uniquePathsWithObstacles(obstacleGrid))
    
    obstacleGrid = [[0,1],[1,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))