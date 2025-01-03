# https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        count = 0
        prefix_sum = [0] * (n)
        for i in range(n-1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            if prefix_sum[i] >= total_sum - prefix_sum[i]:
                count += 1
        return count
    
if __name__ == "__main__":
    s = Solution()
    nums = [10,4,-8,7]
    print(s.waysToSplitArray(nums)) # 2