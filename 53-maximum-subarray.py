# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # using O(n) time complexity
        """
        If the current number is greater than continuous sum of previous numbers, then we start a new subarray.
        keep the maximum updated in each iteration.
        """
        maximum = nums[0]
        current = nums[0]

        for idx in range(1, len(nums)):
            if current + nums[idx] > nums[idx]:
                current += nums[idx]

            else:
                current = nums[idx]
            maximum = max(maximum, current)

        return maximum


if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))