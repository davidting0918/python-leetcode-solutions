# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        for _ in range(k):
            gift = heapq.heappop(heap)
            left = math.floor((-gift) ** (1/2))
            heapq.heappush(heap, -left)

        return -sum(heap)

if __name__ == "__main__":
    s = Solution()
    gifts = [25,64,9,4,100]
    k = 4
    print(s.pickGifts(gifts, k)) # 100