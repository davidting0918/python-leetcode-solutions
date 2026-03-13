# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""
297. Serialize and Deserialize Binary Tree (Hard)

Design an algorithm to serialize and deserialize a binary tree. Serialization
is converting a tree to a string; deserialization reconstructs the tree from
that string.

Approach: Preorder Traversal with Null Markers
- Serialize via preorder DFS, using "N" for null nodes, comma-separated.
- Deserialize by iterating through the token list, recursively building
  left then right subtrees.
- Time: O(n) for both serialize and deserialize
- Space: O(n) for the string / recursion stack
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string via preorder DFS."""
        result = []

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        tokens = data.split(",")
        self.idx = 0

        def dfs() -> TreeNode | None:
            if tokens[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(tokens[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
