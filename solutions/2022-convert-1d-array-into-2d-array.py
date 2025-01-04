# https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-01
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        results = []
        for i in range(m):
            results.append(original[i*n:(i+1)*n])
        return results


if __name__ == "__main__":
    s = Solution()
    original = [1,2,3,4]
    m = 2
    n = 2
    print(s.construct2DArray(original, m, n)) # [[1,2],[3,4]]