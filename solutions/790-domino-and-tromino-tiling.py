class Solution:
    def numTilings(self, n: int) -> int:
        # dp: number of ways to tile 2 x i board
        # dp2: number of ways to tile 2 x i board with upper square missing
        # dp3: number of ways to tile 2 x i board with lower square missing
        modulo = 10**9 + 7

        if n <= 2:
            return 1 if n < 2 else 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp2 = [0] * (n + 1)
        dp2[1] = 1
        dp2[2] = 1
        dp3 = [0] * (n + 1)
        dp3[1] = 1
        dp3[2] = 1

        for i in range(3, n+1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp2[i-1] + dp3[i - 1]) % modulo
            dp2[i] = (dp[i - 2] + dp3[i - 1]) % modulo
            dp3[i] = (dp[i - 2] + dp2[i - 1]) % modulo
            # print(
            #     f"""
            #     dp: {dp}
            #     dp2: {dp2}
            #     dp3: {dp3}
            #     """
            # )

        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numTilings(3))
    print(s.numTilings(1))