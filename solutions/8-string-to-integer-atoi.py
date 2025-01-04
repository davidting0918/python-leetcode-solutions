# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1 if s[0] != '-' else -1
        s = s[1:] if s[0] in ['-', '+'] else s

        for idx in range(len(s)):
            if not s[idx].isdigit():
                s = s[:idx]
                break

        if not s:
            return 0

        if abs(int(s)) >= 2**31:
            return 2**31 if sign == 1 else -2**31
        return int(s) * sign