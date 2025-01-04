# https://leetcode.com/problems/maximum-distance-in-arrays/?envType=daily-question&envId=2024-08-16
from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """
        Logic: 
        - need to find max and min values in two arrays, can't be in the same array
        - keep track of the global max and min values
        - In each array, max(result, array[-1] - min_value, max_value - array[0]) will give the max distance
        - need to update global min and max values
        """
        min_value, max_value = float('inf'), float('-inf')
        result = 0
        for array in arrays:
            result = max(result, array[-1] - min_value, max_value - array[0])
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))