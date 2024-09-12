# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # use set to store allowed characters
        ans = set(allowed)
        result = 0
        for i in words:
            if not set(i) - ans:
                result += 1    
        return result
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])) # 2