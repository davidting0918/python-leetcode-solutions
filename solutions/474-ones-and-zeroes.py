from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # each word seen as a 0-1 knapsack problem

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zero_count = s.count("0")
            one_count = s.count("1")

            for i in range(m, zero_count - 1, -1):
                for j in range(n, one_count - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_count][j - one_count] + 1)

        return dp[m][n]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    s = Solution()
    print(s.findMaxForm(strs, m, n))
