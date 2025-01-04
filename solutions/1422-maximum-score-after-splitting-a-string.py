# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_score = 0
        for i in range(1, n):
            left = s[:i].count("0")
            right = s[i:].count("1")
            max_score = max(max_score, left + right)

        return max_score


if __name__ == "__main__":
    s = Solution()
    string = "011101"
    print(s.maxScore(string)) # 5