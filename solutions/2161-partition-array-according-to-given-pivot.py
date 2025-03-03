# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        less = []
        equal = []

        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)

        return less + equal + greater
    
if __name__ == "__main__":
    s = Solution()
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    print(s.pivotArray(nums, pivot))
