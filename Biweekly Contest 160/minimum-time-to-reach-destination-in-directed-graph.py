# https://leetcode.com/contest/biweekly-contest-160/problems/minimum-time-to-reach-destination-in-directed-graph/description/
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for u, v, start, end in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, start, end))

        max_wait_time = max(end for _, _, _, end in edges) if edges else 0

        queue = [(0, 0)]
        visited = set()

        while queue:
            node, time = queue.pop(0)

            if node == n - 1:
                return time

            if (node, time) in visited:
                continue
            visited.add((node, time))

            if node in graph:
                for nei, start, end in graph[node]:
                    if start <= time <= end:
                        queue.append((nei, time + 1))

            can_use_future_edge = False
            if node in graph:
                for nei, start, end in graph[node]:
                    if end >= time:
                        can_use_future_edge = True
                        break

            if can_use_future_edge and time + 1 <= max_wait_time:
                queue.append((node, time + 1))

        return -1
    
if __name__ == '__main__':
    s = Solution()
    time = 2
    nodes = [[0, 1, 4, 4]]
    print(s.minTime(time, nodes))



        