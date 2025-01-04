# https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        bit_list = [bin(i).count("1") for i in nums]
        target = sorted(nums)

        if nums == target:
            return True

        output = []
        c_bit = bit_list[0]
        c_start = 0
        for i in range(1, n):
            if bit_list[i] != c_bit:
                output.extend(sorted(nums[c_start:i]))
                c_bit = bit_list[i]
                c_start = i

            if i == n - 1:
                output.extend(sorted(nums[c_start:]))

        return output == target



if __name__ == "__main__":
    s = Solution()
    nums = [8,4,2,30,15]
    print(s.canSortArray(nums))  # True