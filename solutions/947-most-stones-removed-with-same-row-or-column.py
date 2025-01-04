# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/?envType=daily-question&envId=2024-08-29
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        parent = {}
        for i, j in stones:
            parent.setdefault(i, i)
            parent.setdefault(~j, ~j)
            union(i, ~j)
        
        return len(stones) - len({find(x) for x in parent})
    
if __name__ == "__main__":
    s = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(s.removeStones(stones))