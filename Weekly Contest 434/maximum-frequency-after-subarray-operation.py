# https://leetcode.com/contest/weekly-contest-434/problems/maximum-frequency-after-subarray-operation/?slug=maximum-frequency-after-subarray-operation&region=global_v2
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # find nums == k
        n = len(nums)
        last_pos = {}
        res = [0 for i in range(n)]
        k_count = [0 for i in range(n+1)]

        for i, num in enumerate(nums):
            k_count[i+1] = k_count[i] + (1 if num == k else 0)
            res[i] = k_count[i]

            if num in last_pos:
                res[i] = max(res[i], res[last_pos[num]] + 1)
            last_pos[num] = i

            continue
        for i in range(n):
            res[i] += (k_count[-1] - k_count[i+1])
        return max(res)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 6, 6, 1, 6, 1]
    k = 1
    print(s.maxFrequency(nums, k))