# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/
class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        """
        Find the minimum step to move source to target
        """
        source = []
        target = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    target.append((i, j))
                elif grid[i][j] != 1:
                    source.append((i, j) * (grid[i][j] - 1))

        # list all combinations of source and target, total combination is len(source)! and use f"{source} to {target}" as key

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,0],[1,1,1],[1,2,1]]
    print(s.minimumMoves(grid))
