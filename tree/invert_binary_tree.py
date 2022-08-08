# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

class DFSSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root

class BFSSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root
