# https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        answer = 0

        if n1 % 2 != 0:
            for i in range(n2):
                if nums2.count(nums2[i]) % 2 == 0:
                    continue
                answer ^= nums2[i]

        if n2 % 2 != 0:
            for i in range(n1):
                if nums1.count(nums1[i]) % 2 == 0:
                    continue
                answer ^= nums1[i]
        
        return answer

if __name__ == '__main__':
    s = Solution()
    num1 = [8,6,29,2,26,16,15,29]
    num2 = [24,12,12]
    print(s.xorAllNums(num1, num2))