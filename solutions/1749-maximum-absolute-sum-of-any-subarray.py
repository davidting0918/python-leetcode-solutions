# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        max_sum = 0
        current_sum = 0
        for i in range(n):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)

        min_sum = float('inf')
        current_sum = 0
        for i in range(n):
            current_sum = min(current_sum + nums[i], nums[i])
            min_sum = min(min_sum, current_sum)
        return max([abs(max_sum), abs(min_sum)])

if __name__ == "__main__":
    s = Solution()
    nums = [1,-3,2,3,-4]
    print(s.maxAbsoluteSum(nums))