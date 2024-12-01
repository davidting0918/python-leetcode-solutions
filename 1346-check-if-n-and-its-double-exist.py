# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ht = {}
        for i in arr:
            if i*2 in ht or i/2 in ht:
                return True
            ht[i] = 1
        return False

if __name__ == "__main__":
    s = Solution()
    arr = [10, 2, 5, 3]
    print(s.checkIfExist(arr))  # True