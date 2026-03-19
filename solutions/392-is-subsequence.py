class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = len(s), len(t)

        dp = [
            [False] * (j + 1) for _ in range(i + 1)
        ]
        for i in range(i + 1):
            for j in range(j + 1):
                if i == 0:
                    dp[i][j] = True
                elif j == 0:
                    dp[i][j] = False
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1] 

        return dp[i][j]


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("axc", "ahbgdc"))