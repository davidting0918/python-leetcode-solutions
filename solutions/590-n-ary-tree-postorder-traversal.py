# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def _recursive(node: Node):
            if not node:
                return result
            for child in node.children:
                _recursive(child)
            result.append(node.val)

        _recursive(root)
        return result
    
    def _iterative(self, root: Node) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        
        return result[::-1]


