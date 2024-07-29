# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1]) * sign
        return result if abs(result) < 2 ** 31 else 0
