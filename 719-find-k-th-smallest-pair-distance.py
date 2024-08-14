# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = low + (high - low) // 2
            count, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,1]
    k = 1
    print(s.smallestDistancePair(nums, k))