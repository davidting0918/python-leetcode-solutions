# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self._isSymmetric(root.left, root.right)
    
    def _isSymmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)