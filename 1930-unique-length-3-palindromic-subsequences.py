# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        answer = 0

        for letter in letters:
            left, right = s.index(letter), s.rindex(letter)
            if left == right:
                continue
            for mid_letter in letters:
                mid = s[left + 1:right].count(mid_letter)
                if mid > 0:
                    answer += 1
            continue
        return answer

if __name__ == "__main__":
    s = Solution()
    string = "aabca"
    print(s.countPalindromicSubsequence(string)) # 3