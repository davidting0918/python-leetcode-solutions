# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/?envType=daily-question&envId=2025-07-29
from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # keep the last position of appearing 1 of each bit
        n = len(nums)
        answers = [0] * n

        max_exp = 30
        last_one = [-1] * max_exp
        for i in range(n - 1, -1, -1):
            for bit in range(max_exp):
                if nums[i] & (1 << bit):
                    last_one[bit] = i
            
            max_pos = i  
            for bit in range(max_exp):
                if last_one[bit] != -1:
                    max_pos = max(max_pos, last_one[bit])
            
            answers[i] = max_pos - i + 1        
        return answers
    

if __name__ == '__main__':
    s = Solution()
    nums = [1,0,2,1,3]

    print(s.smallestSubarrays(nums=nums))