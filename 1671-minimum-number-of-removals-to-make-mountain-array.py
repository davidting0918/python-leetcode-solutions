# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Logic: need to find the longest increasing subsequence from left and right in each position
        need to be strictly increasing and decreasing, so the current index need to be included
        """

        left = [1] * len(nums)

        n = len(nums)

        # find the LIS from left
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)

        # find the LIS from right
        right = [1] * len(nums)

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)

        min_remove = float('inf')
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                subs_length = left[i] + right[i] - 1
                min_remove = min(min_remove, n - subs_length)
        return min_remove


if __name__ == "__main__":
    s = Solution()
    nums = [9,8,1,7,6,5,4,3,2,1]
    print(s.minimumMountainRemovals(nums))
