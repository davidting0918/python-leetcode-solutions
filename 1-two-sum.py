# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index in range(len(nums)):
            completion = target - nums[index]
            if completion in nums[index + 1:]:
                return [index, nums.index(completion, index + 1)]