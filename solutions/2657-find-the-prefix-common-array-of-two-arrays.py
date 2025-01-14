# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2025-01-14
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        answer = []
        for i in range(n):
            answer.append(
                i + 1 - len(set(B[:i+1]) - set(A[:i+1]))
            )
        return answer
    
if __name__ == '__main__':
    s = Solution()
    A = [1,3,2,4]
    B = [3,1,2,4]
    print(s.findThePrefixCommonArray(A, B)) # [1,2,4]