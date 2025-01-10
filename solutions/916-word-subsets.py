# https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-10
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hash_table = {}

        for word in words2:
            for l in set(word):
                if l not in hash_table:
                    hash_table[l] = word.count(l)
                else:
                    hash_table[l] = max(word.count(l), hash_table[l])


        answer = []
        for word in words1:
            add = True
            for l in hash_table:
                if word.count(l) < hash_table[l]:
                    add = False
                    break
            if add:
                answer.append(word)

        return answer

if __name__ == '__main__':
    s = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    print(s.wordSubsets(words1, words2)) # ["apple","google","leetcode"]