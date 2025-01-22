# https://leetcode.com/problems/map-of-highest-peak/description/?envType=daily-question&envId=2025-01-22

from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        waters = []

        n = len(isWater)
        m = len(isWater[0])

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    waters.append((i, j))

        answer = [[float("inf")] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i, j) in waters:
                    answer[i][j] = 0
                    continue
                for water_x, water_y in waters:
                    answer[i][j] = min(answer[i][j], abs(i - water_x) + abs(j - water_y))
        return answer

if __name__ == "__main__":
    s = Solution()  
    iswater = [[0,1],[0,0]]
    print(s.highestPeak(iswater))