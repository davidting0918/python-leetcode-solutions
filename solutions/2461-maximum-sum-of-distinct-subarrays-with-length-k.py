# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k > n:
            return 0

        maximum = 0
        current = 0
        unique = set()
        left = 0

        for right in range(n):

            while nums[right] in unique:
                unique.remove(nums[left])
                current -= nums[left]
                left += 1

            unique.add(nums[right])
            current += nums[right]

            if right - left + 1 == k:
                maximum = max(maximum, current)
                unique.remove(nums[left])
                current -= nums[left]
                left += 1

        return maximum

if __name__ == "__main__":
    s = Solution()
    nums = [5,3,3,1,1]
    k = 3
    print(s.maximumSubarraySum(nums, k))  # 15