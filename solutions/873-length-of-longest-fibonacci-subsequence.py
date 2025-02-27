# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        # since need to check every sub array, so need to be O(n^2)
        # but dp can reduce the number of checks
        index_map = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        # only need to check the current position and the lefter position
        for right in range(n):
            for left in range(right):
                a, b = arr[left], arr[right]
                target = a + b

                if target not in index_map:
                    continue
                target_index = index_map[target]

                if target_index < right:
                    continue

                dp[(right, target_index)] = dp.get((left, right), 2) + 1
                max_len = max(max_len, dp[(right, target_index)])

        return max_len if max_len >= 3 else 0
    
if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,7,8]
    print(s.lenLongestFibSubseq(arr))

