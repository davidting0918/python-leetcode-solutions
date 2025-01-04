# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        
        dp = [0] * n
        index = 0
        dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] - dp[index] > k:
                index += 1
                dp[index] = nums[i]
            else:
                dp[index] = min(dp[index], nums[i])
        
        return index + 1
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,6,1,2,5]
    k = 2
    print(s.partitionArray(nums, k)) # 3