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

    def minSwaps_v2(self, nums: list[int]) -> int:
        total_one = sum(nums)
        n = len(nums)
        max_one_in_window = current_one = sum(nums[:total_one])

        print(f"Range: {total_one} to {n + total_one}")
        for i in range(total_one, n + total_one):  # need to loop to n + total_one to cover circular array
            current_one += nums[i % n]
            current_one -= nums[(i - total_one ) % n]
            print(f"Add index: {i % n}, Remove index: {(i - total_one + n) % n}, Current one: {current_one}")
            max_one_in_window = max(max_one_in_window, current_one)
        return total_one - max_one_in_window


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,0,1]
    print(s.minSwaps_v2(nums))

    nums = [1, 0, 0, 0, 0, 1, 0, 1]
    print(s.minSwaps_v2(nums))