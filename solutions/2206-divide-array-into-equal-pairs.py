# https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17

from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1
        
        for i in count_dict.values():
            if i % 2 != 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.divideArray([3, 2, 3, 2, 2, 2]))