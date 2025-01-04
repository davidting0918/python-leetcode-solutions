# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12
from typing import List
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
    