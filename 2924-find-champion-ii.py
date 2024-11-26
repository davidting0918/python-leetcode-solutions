# https://leetcode.com/problems/find-champion-ii/
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker_team_count = [0] * n

        for i in edges:
            weaker_team_count[i[1]] += 1

        candidates = [i for i in range(n) if weaker_team_count[i] == 0]

        return candidates[0] if len(candidates) == 1 else -1

if __name__ == "__main__":
    s = Solution()
    n = 3
    edges = [[0, 1], [1, 2]]