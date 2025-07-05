# https://leetcode.com/contest/biweekly-contest-160/problems/minimum-time-to-reach-destination-in-directed-graph/description/
from typing import List
import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for u, v, start, end in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, start, end))

        heap = [(0, 0)]
        visited = {}

        while heap:
            time, node = heapq.heappop(heap)

            # if reach to endpoint, return the result
            if node == n - 1:
                return time

            # do not need to revisit the point
            if node in visited and visited[node] <= time:
                continue
            visited[node] = time

            if node in graph:
                for nei, start, end in graph[node]:

                    # can only pass throught the node that end time > current time
                    if end < time:
                        continue  
                    
                    
                    if time < start:
                        heapq.heappush(heap, (start + 1, nei))
                    else:
                        # wait till the node is open
                        heapq.heappush(heap, (time + 1, nei))

        return -1
    
if __name__ == '__main__':
    s = Solution()
    time = 2
    nodes = [[0, 1, 4, 4]]
    print(s.minTime(time, nodes))



        