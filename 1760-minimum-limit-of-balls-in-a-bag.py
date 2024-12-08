# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/?envType=daily-question&envId=2024-12-08
from typing import List
import math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            operations = 0
            for num in nums:
                operations += math.ceil(num / mid) - 1
            if operations > maxOperations:
                left = mid + 1
            else:
                right = mid
            continue
        return left

if __name__ == "__main__":
    s = Solution()
    nums = [5, 17]
    maxOperations = 2
    print(s.minimumSize(nums, maxOperations)) # 3