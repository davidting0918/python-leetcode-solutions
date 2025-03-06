# https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2

        nums = [i for num in grid for i in num]
        set_nums = set(nums)

        missing = n * (n + 1) // 2 - sum(set_nums)
        repeated = sum(nums) - sum(set_nums)
        return [
            repeated,
            missing
        ]

if __name__ == "__main__":
    s = Solution()
    grid = [[1,3],[2,2]]
    print(s.findMissingAndRepeatedValues(grid))