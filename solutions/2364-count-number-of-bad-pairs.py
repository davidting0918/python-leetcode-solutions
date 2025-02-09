# https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        hash_table = {}
        for i in range(n):
            num = nums[i] - i
            hash_table[num] = hash_table.get(num, 0) + 1

        answers = 0
        for i in hash_table:
            answers += (n - hash_table[i]) * (n - hash_table[i] - 1) // 2

        return answers

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,3,3]
    print(s.countBadPairs(nums))