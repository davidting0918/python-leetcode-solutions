from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(sub):
            rob, not_rob = 0, 0
            for num in sub:
                # rob current = previous not_rob + current value
                # not rob current = best of previous either choice
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        return max(helper(nums[:-1]), helper(nums[1:]))


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))
    print(s.rob([1,2,3]))
