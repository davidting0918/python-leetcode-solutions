# https://leetcode.com/problems/path-with-maximum-probability/description/?envType=daily-question&envId=2024-08-27
from typing import List
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Use Dijkstra's algorithm to find the maximum probability path and when dealing with prob, will use log to convert multiplication to addition
        dist = [0] * n
        dist[start_node] = 1

        graph = [[] for _ in range(n)]
        for i, (s, e) in enumerate(edges):
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))

        hq = [(1, start_node)]
        while hq:
            prob, node = max(hq, key=lambda x: x[0])
            hq.remove((prob, node))
            
            if node == end_node:
                return prob
            
            for nei, nei_prob in graph[node]:
                if dist[nei] < dist[node] * nei_prob:
                    dist[nei] = dist[node] * nei_prob
                    hq.append((dist[nei], nei))
        return dist[end_node]
    
    
if __name__ == "__main__":
    s = Solution()
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start_node = 0
    end_node = 2
    print(s.maxProbability(n, edges, succProb, start_node, end_node))