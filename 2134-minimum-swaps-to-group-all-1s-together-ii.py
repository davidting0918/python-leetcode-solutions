# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        total_one = sum(nums)
        n = len(nums)
        min_swap = float("inf")

        # sliding window
        for start in range(n):
            subarray = nums[start:start + total_one]

            if start + total_one > n:
                subarray += nums[:total_one - len(subarray)]

            min_swap = min(min_swap, total_one - sum(subarray))
            # print(f"Start: {start}, end: {start + total_one}, Subarray: {subarray}, Min swap: {min_swap}")

        return min_swap


    def ninSwaps_v2(self, nums: list[int]) -> int:
        total_one = sum(nums)
        n = len(nums)
        min_swap = float("inf")

        circular_nums = nums + nums[:total_one]

        # sliding window
        for start in range(2*n - total_one + 1):
            subarray = circular_nums[start:start + total_one]
            min_swap = min(min_swap, total_one - sum(subarray))
            # print(f"Start: {start}, end: {start + total_one}, Subarray: {subarray}, Min swap: {min_swap}")

        return min_swap


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,0,1]
    print(s.minSwaps(nums))


    nums = [1, 0, 0, 0, 0, 1, 0, 1]
    print(s.minSwaps(nums))