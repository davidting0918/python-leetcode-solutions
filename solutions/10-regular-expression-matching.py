# https://leetcode.com/problems/regular-expression-matching/description/
"""
10. Regular Expression Matching (Hard)

Given a string s and a pattern p, implement regular expression matching with
support for '.' (matches any single character) and '*' (matches zero or more
of the preceding element).

Approach: Dynamic Programming (Bottom-Up)
- dp[i][j] = whether s[0..i-1] matches p[0..j-1]
- Base case: dp[0][0] = True (empty string matches empty pattern)
- For '*', either skip the pattern pair (zero occurrences) or match one more
  character if the preceding element matches.
- Time: O(m * n) where m = len(s), n = len(p)
- Space: O(m * n)
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]: does s[:i] match p[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Option 1: zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # Option 2: one or more — preceding element must match s[i-1]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Direct character match or '.' wildcard
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
