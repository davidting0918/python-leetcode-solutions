# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-02
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']

        prefix_sum = [0] * n
        for i in range(n):
            head, tail = words[i][0], words[i][-1]
            prefix_sum[i] = (
                prefix_sum[i-1] + 
                (1 if head in vowels and tail in vowels else 0)
            )

        prefix_sum = [0] + prefix_sum
        output = []
        for query in queries:
            l, r = query
            output.append(prefix_sum[r+1] - prefix_sum[l])
        return output

    
if __name__ == "__main__":
    s = Solution()
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    print(s.vowelStrings(words, queries)) # [2,3,1]