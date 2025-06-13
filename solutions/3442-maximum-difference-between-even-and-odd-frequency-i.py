# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10

class Solution:
    def maxDifference(self, s: str) -> int:
        letters = set(s)

        even_min = float('inf')
        odd_max = 0

        for letter in letters:
            letter_count = s.count(letter)
            if letter_count % 2 == 0:
                even_min = min(even_min, letter_count)
            else:
                odd_max = max(odd_max, letter_count)
        return odd_max - even_min


if __name__ == "__main__":
    s = Solution()
    print(s.maxDifference("mmsmsym"))