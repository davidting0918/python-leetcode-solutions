# https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Find all pairs (i, j) such that i < j  and i - nums[i] != j - nums[j]
        """
        n = len(nums)

        hash_table = {}
        for i in range(n):
            num = nums[i] - i
            hash_table[num] = hash_table.get(num, 0) + 1

        answers = 0
        total = 0
        for i in sorted(hash_table.keys()):
            answers += hash_table[i] * (n - hash_table[i] - total)
            total += hash_table[i]
            continue
        return answers

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,3,3]
    print(s.countBadPairs(nums))