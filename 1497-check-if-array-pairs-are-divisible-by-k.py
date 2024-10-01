# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_map = {}
        for i in arr:
            remainder_map[i % k] = remainder_map.get(i % k, 0) + 1

        for re in remainder_map:
            if remainder_map[re] == 0:
                continue
            if re == 0:
                if remainder_map[re] % 2 != 0:
                    return False
                continue
            sup = k - re
            if re == sup:
                if remainder_map[re] % 2 != 0:
                    return False
            elif sup not in remainder_map:
                return False
            else:
                if remainder_map[re] != remainder_map[sup]:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,10,6,7,8,9]
    k = 5

    print(s.canArrange(arr, k))