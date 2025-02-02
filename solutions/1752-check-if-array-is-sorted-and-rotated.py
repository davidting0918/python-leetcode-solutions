# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        target = sorted(nums)

        if target == nums:
            return True

        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return target == nums[i:] + nums[:i]

if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.check(nums)) # True