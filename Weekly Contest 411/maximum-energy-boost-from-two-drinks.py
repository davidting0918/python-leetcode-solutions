# https://leetcode.com/contest/weekly-contest-411/problems/maximum-energy-boost-from-two-drinks/description/
from typing import List
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:

        n = len(energyDrinkA)
        dpA = [0] * n
        dpB = [0] * n

        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        for i in range(1, n):
            dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-1] + energyDrinkA[i] - energyDrinkB[i - 1])
            dpB[i] = max(dpA[i-1] + energyDrinkB[i] - energyDrinkA[i - 1], dpB[i-1] + energyDrinkB[i])

        return max(dpA[-1], dpB[-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnergyBoost([4,6,4,3,4,3,5,6,5], [3,5,5,6,5,6,3,3,4]))