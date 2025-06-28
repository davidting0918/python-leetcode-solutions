# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # since need subsequence, so the list to not need to neibour.
        # so sort twice to get the answer, first by value, then by index.
        index_list = [
            (index, num) for index, num in enumerate(nums)
        ]
        sorted_index_list = sorted(index_list, key=lambda x: x[1], reverse=True) # descending
        answer = sorted(sorted_index_list[:k], key=lambda x: x[0]) # ascending
        return [num for _, num in answer]

if __name__ == "__main__":
    s = Solution()
    nums = [50,-75]
    k = 2
    print(s.maxSubsequence(nums, k))