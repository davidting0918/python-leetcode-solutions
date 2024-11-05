# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2024-11-05
class Solution:
    def minChanges(self, s: str) -> int:

        n = len(s)
        total_changes = 0
        for i in range(1, n+1, 2):
            sub = s[i-1: i+1]
            if sub != "00" and sub != "11":
                total_changes += 1
            continue

        return total_changes


if __name__ == "__main__":
    s = Solution()
    print(s.minChanges("0000"))