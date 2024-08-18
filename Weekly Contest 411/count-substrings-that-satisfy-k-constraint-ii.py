# https://leetcode.com/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/description/
from typing import List
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        results = []
        for query in queries:
            total = 0
            sub_n = query[1] - query[0] + 1
            for length in range(1, sub_n + 1):
                for i in range(query[0], query[1] - length + 1):
                    substring = s[i:i+length]
                    if substring.count("1") <= k or substring.count("0") <= k:
                        total += 1
            results.append(total)
        return results