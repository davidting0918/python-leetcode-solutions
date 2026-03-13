"""
124. Binary Tree Maximum Path Sum (Hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
has an edge. A node can only appear in the path at most once.
Return the maximum path sum of any non-empty path.

Approach: DFS Post-order
- At each node, compute the max "gain" if we extend a path through it
  (node.val + max(left_gain, right_gain, 0)).
- Meanwhile, check if the path passing THROUGH this node (left + node + right)
  is the global max.
- Key insight: the gain returned upward can only include ONE branch (or none),
  but the global max can include both branches.
- Time: O(n)
- Space: O(h) recursion stack, h = height
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = max(dfs(node.left), 0)   # ignore negative branches
            right = max(dfs(node.right), 0)

            # Path through this node as the "turning point"
            self.ans = max(self.ans, node.val + left + right)

            # Return max gain extending upward (only one branch)
            return node.val + max(left, right)

        dfs(root)
        return self.ans
