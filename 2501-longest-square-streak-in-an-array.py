# https://leetcode.com/problems/longest-square-streak-in-an-array/description/
from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        output = {}

        sorted_nums = sorted(nums)
        for num in sorted_nums:
            if num in output:
                output[num ** 2] = output[num] + 1
            else:
                output[num ** 2] = 1

        max_length = max(output.values())
        return max_length if max_length != 1 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.longestSquareStreak([4,3,6,16,8,2]))  # 1
