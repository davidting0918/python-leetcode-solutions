# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: TreeNode, level: int):
            if node is None:
                return
            if level == len(output):
                output.append(0)
            output[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        output = []
        dfs(root, 0)
        sorted_output = sorted(output, reverse=True)

        return sorted_output[k - 1] if k <= len(sorted_output) else -1
