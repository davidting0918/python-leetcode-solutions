# https://leetcode.com/contest/weekly-contest-431/problems/maximum-subarray-with-equal-products/description/
from typing import List
from math import gcd
from functools import reduce

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0

        for start in range(n):
            c_gcd = nums[start]
            c_lcm = nums[start]
            c_pro = nums[start]
            for end in range(start + 1, n):
                if end > start:
                    c_gcd = gcd(c_gcd, nums[end])
                    c_lcm = self.lcm(c_lcm, nums[end])
                    c_pro *= nums[end]

                if c_pro == c_gcd * c_lcm:
                    max_length = max(max_length, end - start + 1)

        return max_length

    def lcm(self, a: int, b: int) -> int:
        return a * b // gcd(a, b)

if __name__ == "__main__":
    s = Solution()
