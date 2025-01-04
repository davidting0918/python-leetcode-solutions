# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=daily-question&envId=2024-08-04

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        subarray_sum = []
        for start in range(n + 1):
            for end in range(start + 1, n + 1):
                subarray_sum.append(prefix_sum[end] - prefix_sum[start])
        subarray_sum.sort()
        return sum(subarray_sum[left - 1:right]) % MOD

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    print(s.rangeSum(nums, n, left, right))