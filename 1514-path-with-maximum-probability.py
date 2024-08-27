# https://leetcode.com/problems/path-with-maximum-probability/description/?envType=daily-question&envId=2024-08-27
from typing import List
import math
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Use Dijkstra's algorithm to find the maximum probability path and when dealing with prob, will use log to convert multiplication to addition
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            log_prob = -math.log(prob)
            graph[a].append((b, log_prob))
            graph[b].append((a, log_prob))

        pq = [(0, start_node)]

        probs = [float('inf')] * n
        probs[start_node] = 0

        while pq:
            max_index = min(range(len(pq)), key=lambda i: pq[i][0])
            current_prob, current_node = pq.pop(max_index)
            if current_node == end_node:
                return math.exp(-current_prob)
            for nei, nei_prob in graph[current_node]:
                new_prob = current_prob + nei_prob
                if new_prob < probs[nei]:
                    probs[nei] = new_prob
                    pq.append((new_prob, nei))
        return 0
    
    
if __name__ == "__main__":
    s = Solution()
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start_node = 0
    end_node = 2
    print(s.maxProbability(n, edges, succProb, start_node, end_node))