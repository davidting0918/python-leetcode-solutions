# https://leetcode.com/contest/biweekly-contest-150/problems/sum-of-good-numbers/description/
from typing import List
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:

        n = len(nums)

        answer = 0
        for i in range(n):
            if i + k < n:
                if nums[k + i] >= nums[i]:
                    continue

            if i - k >= 0:
                if nums[i - k] >= nums[i]:
                    continue

            answer += nums[i]
        return answer

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 2, 1, 5, 4]
    k = 2
    print(s.sumOfGoodNumbers(nums, k))
