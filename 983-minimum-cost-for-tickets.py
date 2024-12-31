# https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=daily-question&envId=2024-12-31
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        dp = [0] * (max_day + 1)

        for day in range(1, max_day + 1):
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2]
                )
        return dp[max_day]


if __name__ == "__main__":
    s = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(s.mincostTickets(days, costs)) # 11