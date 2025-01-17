# https://leetcode.com/problems/neighboring-bitwise-xor/description/?envType=daily-question&envId=2025-01-17
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        value = {
            0: {
                0: 0,
                1: 1
            },
            1: {
                0: 1,
                1: 0
            }
        }

        start = 0
        current = 0
        for i in range(n):
            current = value[current][derived[i]]
        return current == start

if __name__ == '__main__':
    s = Solution()
    derived = [1,1,0]
    print(s.doesValidArrayExist(derived)) # True