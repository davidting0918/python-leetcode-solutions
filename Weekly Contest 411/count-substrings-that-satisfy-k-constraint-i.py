# https://leetcode.com/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-i/description/
from typing import List
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """
        Simple brute force solution
        """

        total = 0
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                substring = s[i:i+length]
                if substring.count("1") <= k or substring.count("0") <= k:
                    total += 1

        return total

if __name__ == "__main__":
    s = Solution()
    print(s.countKConstraintSubstrings("10101", 1))