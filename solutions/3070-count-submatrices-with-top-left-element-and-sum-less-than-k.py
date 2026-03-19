from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])

        prefix_sum = [
            [0 for _ in range(col)] for _ in range(row)
        ]

        ans = 0
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    prefix_sum[i][j] = grid[i][j]
                elif i == 0:
                    prefix_sum[i][j] = prefix_sum[i][j-1] + grid[i][j]
                elif j == 0:
                    prefix_sum[i][j] = prefix_sum[i-1][j] + grid[i][j]
                else:
                    prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + grid[i][j]

                if prefix_sum[i][j] <= k:
                    ans += 1
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSubmatrices([[7,6,3],[6,6,1]], 18))
    print(s.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20))