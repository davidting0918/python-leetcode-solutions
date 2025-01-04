# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=daily-question&envId=2024-12-16
from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        
        return nums 
    
if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    print(s.getFinalState(nums, k, multiplier))