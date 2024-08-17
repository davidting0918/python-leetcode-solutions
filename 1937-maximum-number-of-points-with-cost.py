# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/?envType=daily-question&envId=2024-08-17
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # use two way search to find the max value
        """
        Logic: we will split the problem into from left or right,
        大改可以理解為每一部都考慮如果要從前一行的這個位置到我現在這個位置可能可以得到的最大分數，
        """
        r_num = len(points)
        c_num = len(points[0])
        dp = points[0]
        for i in range(1, r_num):
            left_max = [0] * c_num
            left_max[0] = dp[0]

            for j in range(1, c_num):
                left_max[j] = max(left_max[j-1] - 1, dp[j])

            
            right_max = [0] * c_num
            right_max[c_num-1] = dp[c_num-1]

            for j in range(c_num-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, dp[j])
    
            for j in range(c_num):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    points = [[4,4,2,2,1],[5,5,2,1,2],[3,1,5,5,2],[3,2,0,0,3]]
    print(s.maxPoints(points))