# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
class Solution:
    def minSwaps(self, s: str) -> int:
        # logic: '[' mean +1, ']' mean -1. if the sum is negative, find the next '[' to swap
        swap_time = 0
        string_sum = 0
        for i in s:
            if i == '[':
                string_sum += 1
            elif i == ']':
                string_sum -= 1

            if string_sum < 0:
                swap_time += 1
                string_sum += 2
        return swap_time

if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps(']]][[['))
