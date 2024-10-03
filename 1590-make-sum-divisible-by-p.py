# https://leetcode.com/problems/make-sum-divisible-by-p/description/
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # if the sum of the original nums is divisible by p, then return 0
        target = sum(nums) % p
        
        if target == 0:
            return 0
        
        n = len(nums)
        min_length = n
        current_sum = 0
        prefix_sum = {0: -1}
        
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            
            find = (current_sum - target) % p
            continue
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,1,4,2]
    p = 6
    print(s.minSubarray(nums, p))