# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # cousins are nodes at the same level but different parents
        def dfs_sum(node: TreeNode, level: int):
            if node is None:
                return
            output[level] = output.get(level, 0) + node.val
            dfs_sum(node.left, level + 1)
            dfs_sum(node.right, level + 1)
        def dfs_minus(node: TreeNode, level: int, current_value: int):
            if node is None:
                return

            node.val = output[level] - current_value

            next_value = 0
            if node.right:
                next_value += node.right.val
            if node.left:
                next_value += node.left.val
            dfs_minus(node.left, level + 1, next_value)
            dfs_minus(node.right, level + 1, next_value)

        output = {}
        dfs_sum(root, 0)
        dfs_minus(root, 0, root.val)
        return root

