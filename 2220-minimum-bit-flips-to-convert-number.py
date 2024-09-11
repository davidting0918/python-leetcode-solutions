# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        if len(start) < len(goal):
            start = '0' * (len(goal) - len(start)) + start

        elif len(goal) < len(start):
            goal = '0' * (len(start) - len(goal)) + goal

        result = 0
        for s, g in zip(start, goal):
            if s != g:
                result += 1
        return result
    

if __name__ == "__main__":
    s = Solution()
    print(s.minBitFlips(start=10, goal=7))