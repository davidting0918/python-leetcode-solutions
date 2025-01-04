# https://leetcode.com/problems/extra-characters-in-a-string/description/
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)

        n = len(s)

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    string = "sayhelloworld"
    dictionary = ["hello","world"]

    print(s.minExtraChar(string, dictionary))
