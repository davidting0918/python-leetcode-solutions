# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09
from operator import contains
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        sorted_words = sorted(words, key = lambda x: len(x), reverse = True)

        answer = 0
        for i in sorted_words:
            if len(pref) > len(i):
                break

            if i.startswith(pref):
                answer += 1

        return answer


if __name__ == "__main__":
    s = Solution()
    words = ["pay","attention","practice","attend"]
    pref = 'at'
    print(s.prefixCount(words, pref)) # 3