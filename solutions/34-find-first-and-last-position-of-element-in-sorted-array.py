# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        n = len(nums)
        

        left = nums.index(target)
        
        for i in range(n-1, -1, -1):
            if nums[i] == target:
                right = i
                return [left, right]
        return
    
if __name__ == "__main__":
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(s.searchRange(nums, target))