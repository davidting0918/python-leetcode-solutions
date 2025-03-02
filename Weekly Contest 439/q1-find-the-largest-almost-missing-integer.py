# https://leetcode.com/contest/weekly-contest-439/problems/find-the-largest-almost-missing-integer/description/
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_count = {}
        for start in range(n-k+1):
            end = start + k

            subarray = set(nums[start:end])
            for num in subarray:
                if num not in num_count:
                    num_count[num] = 1
                else:
                    num_count[num] += 1
            print(nums[start:end])

        max_num = -1
        for i in num_count:
            if num_count[i] == 1:
                max_num = max(max_num, i)
        return max_num

if __name__ == "__main__":
    s = Solution()
    nums = [0, 0]
    k = 2
    print(s.largestInteger(nums, k))