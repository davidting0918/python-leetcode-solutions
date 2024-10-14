# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
from typing import List
import math
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0
        max_heap = []

        for i in nums:
            heapq.heappush(max_heap, -i)

        for _ in range(k):

            max_val = -heapq.heappop(max_heap)
            result += max_val
            heapq.heappush(max_heap, -math.ceil(max_val / 3))
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxKelements([1,10,3,3,3], 3))