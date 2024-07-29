# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        full_list = sorted(nums1 + nums2)
        mid_index = len(full_list) // 2

        if len(full_list) % 2 == 0:
            return (full_list[mid_index - 1] + full_list[mid_index]) / 2
        else:
            return full_list[mid_index]
    
    def findMedianSortedArrays_with_binary_search(self, nums1: list[int], nums2: list[int]) -> float:
        return