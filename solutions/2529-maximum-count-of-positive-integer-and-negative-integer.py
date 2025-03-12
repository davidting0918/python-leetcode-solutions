# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=daily-question&envId=2025-03-12
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for i in nums:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1
        return max(pos, neg)
    
if __name__ == '__main__':
    s = Solution()