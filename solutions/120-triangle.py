# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Logic: from bottom to top, since in level -1 the number itself if the minimum path sum, then in level -2,
        the number itself plus the minimum of the next level is the minimum path sum, and so on.
        """
        dp = [0] * (len(triangle) + 1)
        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
                print(dp)
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))