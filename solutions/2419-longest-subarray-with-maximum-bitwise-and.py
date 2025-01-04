# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_length = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 0
        
        return max_length
    
    
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 3, 2, 2]
    print(s.longestSubarray(nums))
    