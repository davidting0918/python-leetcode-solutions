# https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # the question is to find the non-continuous k houses which has min of max value among the robbed houses
        # binary search
        # if can_rob, then try to use a smaller mid
        n = len(nums)
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            if self.can_rob(nums, k, mid, n):
                right = mid
            else:
                left = mid + 1
        return left
    
    def can_rob(self, nums: List[int], k: int, mid: int, n: int) -> bool:
        # check if we can rob k houses with min value mid
        
        prev_robbed = False
        for i in range(n):
            if nums[i] <= mid:
                if not prev_robbed:
                    prev_robbed = True
                    k -= 1
                    continue
        
            prev_robbed = False

        return k <= 0
    

if __name__ == "__main__":
    s = Solution()
    print(s.minCapability([2,7,9,3,1], 2))
