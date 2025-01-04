# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = s1.split()
        lst2 = s2.split()
        
        output = []
        for i in lst1:
            if lst1.count(i) == 1 and i not in lst2:
                output.append(i)
        
        for i in lst2:
            if lst2.count(i) == 1 and i not in lst1:
                output.append(i)
        return output

if __name__ == "__main__":
    s = Solution()
    s1 = "abcd def abcd xyz"
    s2 = "ijk def ijk"
    print(s.uncommonFromSentences(s1, s2))  # ["xyz"]