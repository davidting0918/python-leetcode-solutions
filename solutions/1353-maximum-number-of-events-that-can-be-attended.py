# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=daily-question&envId=2025-07-07
from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[0])

        heap = []

        index = 0
        n = len(events)
        max_day = max(i for _, i in events)
        
        count = 0
        for day in range(1, max_day + 1):

            # add event start at today in the heap
            # because of index < n, so do not need to iterate whole list from the beginning
            while index < n and events[index][0] == day:
                heapq.heappush(heap, events[index][1])
                index += 1

            # remove the passed event
            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count += 1
        return count
    

if __name__ == "__main__":
    s = Solution()
    events = [[1,2],[2,3],[3,4],[1,2]]
    print(s.maxEvents(events=events))