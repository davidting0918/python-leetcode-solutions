# https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def _recursive(node: TreeNode):
            if not node:
                return
            
            if node.left:
                _recursive(node.left)
            if node.right:
                _recursive(node.right)
            result.append(node.val)

        _recursive(root)
        return result
    
    def _iterative(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        stack = [root]

        while stack:
            n = stack.pop()
            result.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return result[::-1]
    








