from ast import mod
from pickletools import read_uint1
from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid),len(grid[0])
        modulo = 12345
        all_nums = [grid[i][j] for i in range(m) for j in range(n)]

        total = m * n
        prefix = [1] * total  # not include current index
        for i in range(1, total):
            prefix[i] = (prefix[i - 1] * all_nums[i - 1]) % modulo

        suffix = [1] * total
        for i in range(total - 2, -1, -1):
            suffix[i] = (suffix[i+1] * all_nums[i + 1]) % modulo
        
        result = [(prefix[i] * suffix[i]) % modulo for i in range(total)]
        answers = [
            [result[i * n + j] for j in range(n)] for i in range(m)
        ]
        return answers

if __name__ == "__main__":
    s = Solution()
    print(s.constructProductMatrix([[1,2],[3,4]]))
    print(s.constructProductMatrix([[12345],[2],[1]]))