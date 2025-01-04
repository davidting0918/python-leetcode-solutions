# https://leetcode.com/problems/max-chunks-to-make-sorted/?envType=daily-question&envId=2024-12-19
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Solution logic: if the max number in the chunk is equal to the index of the chunk, then we can split the chunk
        chunks = 0
        
        max_num = 0
        for i, num in enumerate(arr):
            max_num = max(max_num, num)
            if max_num == i:
                chunks += 1

        return chunks
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,0,3,2,5,4]
    print(s.maxChunksToSorted(nums))