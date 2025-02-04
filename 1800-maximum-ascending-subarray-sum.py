# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        answer = 0
        temp = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                answer = max(answer, temp)
                temp = nums[i]

        answer = max(answer, temp)
        return answer

if __name__ == "__main__":
    s = Solution()
    nums = [10,20,30,5,10,50]
    print(s.maxAscendingSum(nums))