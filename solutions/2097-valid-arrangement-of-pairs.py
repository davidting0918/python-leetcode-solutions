# https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-11-30
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graphs = {}
        in_count = {}
        out_count = {}
        for pair in pairs:
            node_list = graphs.get(pair[0], [])
            node_list.append(pair[1])
            graphs[pair[0]] = node_list
            in_count[pair[1]] = in_count.get(pair[1], 0) + 1
            out_count[pair[0]] = out_count.get(pair[0], 0) + 1

        # decide start point
        start_node = None
        for node in graphs:
            if out_count.get(node, 0) > in_count.get(node, 0):  # Out-degree > In-degree
                start_node = node
                break

        if start_node is None:
            start_node = pairs[0][0]

        # use hierholzer algorithm to find euler path
        path = []
        stack = [start_node]

        while stack:
            while graphs.get(stack[-1]):
                next_node = graphs[stack[-1]].pop()
                stack.append(next_node)
            path.append(stack.pop())

        path.reverse()
        return [[path[i], path[i+1]] for i in range(len(path) - 1)]

if __name__ == "__main__":
    s = Solution()
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    print(s.validArrangement(pairs))  # [[5,1],[4,5],[11,9],[9,4]]