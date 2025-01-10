# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]):
                    answer += 1
                    continue
                
                if words[j].endswith(words[i]):
                    answer += 1
                    continue
        return answer
    
if __name__ == "__main__":
    s = Solution()
    words = ["abab","ab"]
    print(s.countPrefixSuffixPairs(words)) # 4