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
                    for _ in range(grid[i][j] - 1):
                        source.append((i, j))

        # list all combinations of source and target, total combination is len(source)! and use f"{source} to {target}" as key
        results = []
        self._recursive_run(len(source), [False] * len(source), [], results, source, target)
        return min(results)
    
    def _recursive_run(self, n, used, current, results, s, t):
        if len(current) == n:
             results.append(
                 sum(
                    abs(s[i][0] - t[j][0]) + abs(s[i][1] - t[j][1])
                    for i, j in enumerate(current)
                 )
             )
        
        for i in range(n):
            if not used[i]:
                used[i] = True
                current.append(i)
                self._recursive_run(n, used, current, results, s, t)
                current.pop()
                used[i] = False
        

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,0],[1,1,1],[1,2,1]]
    print(s.minimumMoves(grid))
    
    grid = [[1,3,0],[1,0,0],[1,0,3]]
    print(s.minimumMoves(grid))
