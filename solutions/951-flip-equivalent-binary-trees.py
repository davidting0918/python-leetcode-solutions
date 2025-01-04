# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def flip(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return (flip(node1.left, node2.left) and flip(node1.right, node2.right)) or (flip(node1.left, node2.right) and flip(node1.right, node2.left))
        return flip(root1, root2)



if __name__ == "__main__":
    pass