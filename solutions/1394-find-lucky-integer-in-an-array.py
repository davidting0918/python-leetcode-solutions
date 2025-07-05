# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        candidates = sorted(list(set(arr)), reverse=True)
        for candidate in candidates:
            if candidate == arr.count(candidate):
                return candidate
        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.findLucky([2,2,3,4]))