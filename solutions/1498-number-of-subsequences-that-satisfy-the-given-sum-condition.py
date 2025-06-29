# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=daily-question&envId=2025-06-29
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()  # ascending
        left, right = 0, n - 1
        count = 0

        # two pointer solution will reduce to O(n) rather than double loop

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return count % (10**9 + 7)
    
if __name__ == "__main__":
    s = Solution()
    nums = [3, 3, 6, 8]
    target = 10
    print(s.numSubseq(nums, target))