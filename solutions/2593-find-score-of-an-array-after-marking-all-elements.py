# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/?envType=daily-question&envId=2024-12-13
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # only use O(n) time complexity to iterate through the array,
        # and use marked to check whether current index can be usde
        n = len(nums)
        scores = 0
        marked = [
            False for _ in range(n)
        ]
        
        # sort index using its position value, later use its index
        sorted_index = sorted(range(n), key=lambda i: nums[i])

        for index in sorted_index:
            if marked[index]:
                continue

            scores += nums[index]
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            
            if index < n - 1:
                marked[index + 1] = True
        return scores
    
if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3,4,5,2]
    print(s.findScore(nums=nums))