# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/?envType=daily-question&envId=2026-03-27
from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        shift = k % n

        if shift == 0:
            return True

        for i, row in enumerate(mat):
            if i % 2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[-shift:] + row[:-shift]

            if shifted != row:
                return False

        return True

if __name__ == '__main__':
    s = Solution()

    # Example 1
    assert s.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 4) == False
    # Example 2
    assert s.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2) == True
    # Example 3
    assert s.areSimilar([[2,2],[2,2]], 3) == True

    print("All test cases passed!")
