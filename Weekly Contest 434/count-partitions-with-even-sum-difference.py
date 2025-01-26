# https://leetcode.com/contest/weekly-contest-434/problems/count-partitions-with-even-sum-difference/description/
from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]


        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        answer = 0
        for i in range(1, n):
            if abs(prefix_sum[i] - suffix_sum[i]) % 2 == 0:
                answer += 1

        return answer

if __name__ == "__main__":
    s = Solution()
    nums = [10, 10, 3, 7, 6]
    print(s.countPartitions(nums)) # 3
