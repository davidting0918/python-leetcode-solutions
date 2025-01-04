# https://leetcode.com/problems/maximum-product-subarray/?envType=study-plan-v2&envId=top-100-liked
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # in dp, first term is min, second term is max
        dp = [
            [0, 0] for _ in range(n)
        ]
        dp[0] = [nums[0], nums[0]]

        for i in range(1, n):
            # need to calculate min and max for each element
            dp[i][0] = min(
                nums[i],
                dp[i - 1][0] * nums[i],
                dp[i - 1][1] * nums[i]
            )

            dp[i][1] = max(
                nums[i],
                dp[i - 1][0] * nums[i],
                dp[i - 1][1] * nums[i]
            )

        return max([x[1] for x in dp])
if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([-2,3,-4]))

