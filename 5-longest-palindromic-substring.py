class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or self.is_palindrome(s):
            return s

        for length in range(len(s) - 1, 1, -1):
            for start in range(len(s) - length + 1):
                if self.is_palindrome(s[start:start + length]):
                    return s[start:start + length]
    

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    

if __name__ == "__main__":
    s = Solution()
    string = "babad"
    print(s.longestPalindrome(string))

    string = "cbbd"
    print(s.longestPalindrome(string))

    string = "a"
    print(s.longestPalindrome(string))

    string = "ac"
    print(s.longestPalindrome(string))