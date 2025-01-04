# https://leetcode.com/problems/modify-graph-edge-weights/description/?envType=daily-question&envId=2024-08-30
from typing import List

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(graph, src, dst) -> int:
            # find the shortest path from source to dest
            dist = [float("-inf")] * n
            dist[src] = 0
            hq = [(0, src, False)]  # total dist, source point, if -1 node in paths

            while hq:
                d, node, neg_in = min(hq, key=lambda x: x[0])
                hq.remove((d, node, neg_in))

                if node == dst:
                    return d, neg_in
                
                if d > dist[node]:
                    continue

                for nei, w in graph[node]:
                    new_d = d + abs(w)
                    if new_d < dist[nei]:
                        dist[nei] = new_d
                        hq.append((new_d, nei))
            return float("-inf")
        
        graph = [[] for _ in range(n)]
        neg_edges = []
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                neg_edges.append(i)
            else:
                graph[u].append((v, w))
                graph[v].append((u, w))

        init_dest, status = dijkstra(graph, source, destination)
        
        if init_dest > target and status == True:
            return []
        
        if init_dest < target and status == False:
            return []
    

if __name__ == "__main__":
    s = Solution()

    # test case 1
    n = 5
    edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
    source = 0
    destination = 1
    target = 5

    print(s.modifiedGraphEdges(n, edges, source, destination, target))