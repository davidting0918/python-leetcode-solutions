# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = nums[1] - nums[0], nums[-1] - nums[0]
    

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,1]
    k = 1
    print(s.smallestDistancePair(nums, k))