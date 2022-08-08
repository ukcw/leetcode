# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node1: Optional[TreeNode], node2: Optional[TreeNode]) \
                -> bool:
            if not node1 and node2:
                return False
            elif node1 and not node2:
                return False
            elif not node1 and not node2:
                return True
            else:
                return node1.val == node2.val \
                        and check(node1.left, node2.left) \
                        and check(node1.right, node2.right)

        return check(p, q)

    def eloquentSolution(self, p: Optional[TreeNode], q:Optional[TreeNode]) \
            -> bool:
        if p and q:
            return p.val == q.val \
                    and self.eloquentSolution(p.left, q.left) \
                    and self.eloquentSolution(p.right, q.right)

        return p is q
