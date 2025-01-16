# https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # x ^ x = 0, 0 ^ x = x
        
        n1 = len(nums1)
        n2 = len(nums2)

        answer = 0

        hash_table = {}

        for i in nums1:
            hash_table[i] = hash_table.get(i, 0) + n2

        for i in nums2:
            hash_table[i] = hash_table.get(i, 0) + n1

        for i in hash_table:
            if hash_table[i] % 2 == 1:
                answer ^= i

        return answer

if __name__ == '__main__':
    s = Solution()
    num1 = [8,6,29,2,26,16,15,29]
    num2 = [24,12,12]
    print(s.xorAllNums(num1, num2))