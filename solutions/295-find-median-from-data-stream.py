"""
295. Find Median from Data Stream (Hard)
https://leetcode.com/problems/find-median-from-data-stream/

Design a data structure that supports addNum(num) and findMedian() efficiently.

Approach: Two Heaps (Max-Heap + Min-Heap)
- max_heap (inverted): stores the SMALLER half of numbers.
- min_heap: stores the LARGER half of numbers.
- Balance: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1.
- Median = top of max_heap (if odd), or average of both tops (if even).
- Time: O(log n) per addNum, O(1) per findMedian.
- Space: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self):
        # max_heap: store negated values (Python only has min-heap)
        self.max_heap = []  # smaller half
        self.min_heap = []  # larger half

    def addNum(self, num: int) -> None:
        # Always push to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Ensure max_heap top <= min_heap top
        if self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balance sizes: max_heap can have at most 1 more element
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
