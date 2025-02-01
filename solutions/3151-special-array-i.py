# https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01
from math import remainder
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        parity = [0 if nums[0] % 2 == 0 else 1]

        for i in range(1, n):
            remain = nums[i] % 2
            if remain == parity[i-1]:
                return False
            parity.append(remain)
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 1, 6]
    print(s.isArraySpecial(nums))