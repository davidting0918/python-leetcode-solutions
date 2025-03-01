# https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        answer = []
        for i in range(n):
            if nums[i] != 0:
                answer.append(nums[i])

        for i in range(n - len(answer)):
            answer.append(0)
        return answer

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2,1,1,0]
    print(s.applyOperations(nums))