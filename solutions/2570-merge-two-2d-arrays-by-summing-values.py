# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        max_index = max(nums1[-1][0], nums2[-1][0])
        answer = [[i, 0] for i in range(1, max_index+1)]

        for i in nums1:
            answer[i[0]-1][1] += i[1]

        for i in nums2:
            answer[i[0]-1][1] += i[1]

        return [i for i in answer if i[1] != 0]

if __name__ == "__main__":
    s = Solution()
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    print(s.mergeArrays(nums1, nums2))