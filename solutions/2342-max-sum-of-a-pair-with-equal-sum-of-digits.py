# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        hash_table = {}

        for i in range(n):
            digit_sum = sum(
                [int(d) for d in str(nums[i])]
            )
            if digit_sum not in hash_table:
                hash_table[digit_sum] = []

            hash_table[digit_sum].append(nums[i])
        
        answer = 0
        for i in hash_table:
            if len(hash_table[i]) < 2:
                continue
            hash_table[i].sort()
            answer = max(
                answer,
                hash_table[i][-1] + hash_table[i][-2]
            )
        return answer
    
if __name__ == '__main__':
    s = Solution()
    nums = [18,43,36,13,7]
    print(s.maximumSum(nums))