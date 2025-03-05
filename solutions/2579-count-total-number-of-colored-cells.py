# https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05
class Solution:
    def coloredCells(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + ((i-2) * 4 + 4)

        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.coloredCells(4))