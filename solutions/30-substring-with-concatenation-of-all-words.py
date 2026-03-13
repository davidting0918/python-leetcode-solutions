# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""
30. Substring with Concatenation of All Words (Hard)

Given a string s and an array of equal-length words, find all starting indices
of substrings in s that are a concatenation of each word in words exactly once,
in any order.

Approach: Sliding Window with Word-Level Granularity
- Since all words have the same length w, we can slide a window of size
  w * len(words) over s.
- Use w different starting offsets (0, 1, ..., w-1) to cover all alignments.
- For each offset, maintain a word frequency map and slide the window by
  one word at a time, shrinking from the left when a word is over-counted.
- Time: O(n * w) where n = len(s), w = word length
- Space: O(k) where k = number of words
"""

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        # Try each possible starting offset within a word length
        for offset in range(word_len):
            left = offset
            current = Counter()
            matched = 0  # number of words matched so far

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    current[word] += 1
                    matched += 1

                    # Shrink window if a word is over-represented
                    while current[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        matched -= 1
                        left += word_len

                    # All words matched exactly
                    if matched == num_words:
                        result.append(left)
                else:
                    # Reset — word not in dictionary
                    current.clear()
                    matched = 0
                    left = right + word_len

        return result
