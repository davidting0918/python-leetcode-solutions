# https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05
from turtledemo.penrose import start
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # use prefix sum to calculate the cum delta for each letter in each index so far
        n = len(s)
        delta = [0] * (n + 1)

        for shift in shifts:
            start, end, amount = shift
            if amount == 0:
                delta[start] -= 1
                delta[end + 1] += 1
            else:
                delta[start] += 1
                delta[end + 1] -= 1

        cum_delta = 0
        result = ""
        for i in range(n):
            cum_delta += delta[i]
            result += self.get_new_letter(s[i], cum_delta)

        return result

    def get_new_letter(self, letter: str, shift: int) -> str:
        return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

if __name__ == "__main__":
    s = Solution()
    string = 'abc'
    shifts = [[0,1,0],[1,2,1],[0,2,1]]
    print(s.shiftingLetters(string, shifts)) # bcd