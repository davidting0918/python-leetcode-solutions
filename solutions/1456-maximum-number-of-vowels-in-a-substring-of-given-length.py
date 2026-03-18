class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set('aeiou')

        max_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1
        current_vowels = max_vowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i-k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels

if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("abciiidef", 3))