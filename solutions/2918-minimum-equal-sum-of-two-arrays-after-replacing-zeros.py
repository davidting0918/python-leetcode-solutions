# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10

from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        count1 = nums1.count(0)
        count2 = nums2.count(0)
        
        min_sum1 = sum1 + count1
        min_sum2 = sum2 + count2

        if min_sum1 == min_sum2:
            return min_sum1
        elif min_sum1 > min_sum2:
            if count2 == 0:
                return -1
            else:
                return min_sum1
        else:
            if count1 == 0:
                return -1
            else:
                return min_sum2
            
if __name__ == '__main__':
    s = Solution()
    nums1 = [2,0,2,0]
    nums2 = [1,4]
    print(s.minSum(nums1, nums2))