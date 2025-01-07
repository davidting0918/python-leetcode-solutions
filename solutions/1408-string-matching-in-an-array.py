# https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        sorted_words = sorted(words, key=lambda x: len(x))

        answer = []
        for word in sorted_words:
            for index in range(n-1, -1, -1):
                if len(sorted_words[index]) < len(word):
                    break

                if word in sorted_words[index] and word != sorted_words[index]:
                    answer.append(word)
                    break
        return answer

if __name__ == "__main__":
    s = Solution()
    words = ["leetcode","et","code"]
    print(s.stringMatching(words)) #       