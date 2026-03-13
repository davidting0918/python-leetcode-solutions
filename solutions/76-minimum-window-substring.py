"""
76. Minimum Window Substring (Hard)
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.

Approach: Sliding Window with Two Pointers
- Maintain a frequency map of characters needed from t.
- Expand the right pointer to include characters, shrink the left pointer
  when all characters are satisfied.
- Track the minimum window that contains all required characters.
- Time: O(|s| + |t|)
- Space: O(|s| + |t|)
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)  # total chars still needed
        left = 0
        best_left, best_right = 0, float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # All chars satisfied — try shrinking from left
            while missing == 0:
                if right - left < best_right - best_left:
                    best_left, best_right = left, right

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_right == float("inf") else s[best_left : best_right + 1]
