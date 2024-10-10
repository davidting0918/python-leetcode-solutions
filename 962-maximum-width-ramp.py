# https://leetcode.com/problems/maximum-width-ramp/description/
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        
        for i in range(n):
            if not stack or nums[i] <= nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_width = max(max_width, i - stack.pop())
        
        return max_width
    
if __name__ == "__main__":
    s = Solution()
    nums = [6,0,8,2,1,5]
    print(s.maxWidthRamp(nums))  # 4