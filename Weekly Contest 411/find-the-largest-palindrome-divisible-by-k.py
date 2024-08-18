# https://leetcode.com/contest/weekly-contest-411/problems/find-the-largest-palindrome-divisible-by-k/description/
from typing import List
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        max_n = 10**n - 1
        remainder = max_n % k

        for num in range(max_n - remainder, 0, -k):
            str_num = str(num)
            if str_num == str_num[::-1]:
                return str_num



if __name__ == "__main__":
    sol = Solution()
    print(sol.largestPalindrome(9, 4))