# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # logic: if K appear in the second half of the string and op == 1 then will increase 1 count from "a"
        final_length = 2 ** len(operations)

        reverse_time = 0
        for op in operations[::-1]:
            final_length = final_length // 2
            if k > final_length:
                k -= final_length
                if op == 1:
                    reverse_time += 1

        return chr(97 + reverse_time % 26)
    
if __name__ == "__main__":
    s = Solution()
    print(s.kthCharacter(100000000000000, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))