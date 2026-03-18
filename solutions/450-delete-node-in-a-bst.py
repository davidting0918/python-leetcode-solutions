from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            return self._deleteNode(root)

        return root
        
    def _deleteNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # core logic : this function need to return node to let the caller receive and connect to the original parent node
        if not root.left and not root.right:
            return None
        if not root.right:
            return root.left
        if not root.left:
            return root.right

        # if both existed, find the smallest from from 
        current_node = root.right
        while current_node.left:
            current_node = current_node.left
        root.val = current_node.val
        root.right = self.deleteNode(root.right, current_node.val)

        return root 
    