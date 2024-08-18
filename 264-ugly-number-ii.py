# https://leetcode.com/problems/ugly-number-ii/description/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        「醜數」是指其質因數僅限於 2、3 和 5 的正整數。
        Use three pointers to track the next multiple of 2, 3, and 5.
        in each iteration, find the minimum value among the three pointers,
        and move the pointer 1 step forward.
        """
        dp = [0] * n
        dp[0] = 1

        i2 = i3 = i5 = 0

        for i in range(1, n):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if dp[i] == dp[i2] * 2:
                i2 += 1
            if dp[i] == dp[i3] * 3:
                i3 += 1
            if dp[i] == dp[i5] * 5:
                i5 += 1
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(10))