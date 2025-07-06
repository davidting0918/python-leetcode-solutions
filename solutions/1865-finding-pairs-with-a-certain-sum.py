# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/?envType=daily-question&envId=2025-07-06
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = {}
        for i in nums2:
            self.counter[i] = self.counter.get(i, 0) + 1

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] = self.counter.get(self.nums2[index], 0) + 1 

    def count(self, tot: int) -> int:
        count = 0
        for i in self.nums1:
            if tot - i in self.counter:
                count += self.counter[tot - i]

        return count


if __name__ == '__main__':
    nums1 = [1,1,2,2,2,3]
    nums2 = [1,4,5,2,5,4]
    operations = ["count","add","count","count","add","add","count"]
    nums = [[7],[3,2],[8],[4],[0,1],[1,1],[7]]
    s = FindSumPairs(nums1=nums1, nums2=nums2)

    for op, num in zip(operations, nums):
        if op == 'count':
            print(s.count(num[0]))

        else:
            print(s.add(num[0], num[1]))