class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0] * (high + 1)
        dp[0] = 1 # null string should be one condition

        MOD = 10**9 + 7

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD 

        return sum(dp[low:]) % MOD
    

if __name__ == "__main__":
    s = Solution()
    print(s.countGoodStrings(3, 3, 1, 1))
    print(s.countGoodStrings(2, 3, 1, 2))