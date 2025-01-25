# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # use reversed graph to check if a node is safe, and the neighbors of a node is safe
        n = len(graph)

        reversed_graph = [[] for _ in range(n)]

        for i in range(n):
            for j in graph[i]:
                reversed_graph[j].append(i)

        degrees = [len(graph[i]) for i in range(n)]
        queue = [i for i in range(n) if not graph[i]]
        answers = []
        while queue:
            node = queue.pop(0)
            answers.append(node)
            for i in reversed_graph[node]:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i)
            continue


        return sorted(answers)
    
if __name__ == "__main__":
    s = Solution()
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(s.eventualSafeNodes(graph))