# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        answer = 0

        # ascending
        length = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                length += 1
            else:
                answer = max(answer, length)
                length = 1
        answer = max(answer, length)

        # decreasing
        length = 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                length += 1
            else:
                answer = max(answer, length)
                length = 1
        answer = max(answer, length)

        return answer

if __name__ == "__main__":
    s = Solution()
    nums = [1,4,3,3,2]
    print(s.longestMonotonicSubarray(nums))