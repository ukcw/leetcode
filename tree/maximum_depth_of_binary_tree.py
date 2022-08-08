# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode], prevDepth) -> int:
            if not root:
                return prevDepth
            else:
                return max(depth(root.left, 1 + prevDepth),
                        depth(root.right, 1 + prevDepth))

        return depth(root, 0)

class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(0, root)])
        result = 0

        while queue:
            depth, node = queue.popleft()
            if node:
                result = max(result, 1 + depth)

                queue.append((1 + depth, node.left))
                queue.append((1 + depth, node.right))

        return result
