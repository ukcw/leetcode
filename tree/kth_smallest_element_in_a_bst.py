# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorderTraversal(root: Optional[TreeNode]) -> List[Optional[int]]:
            if root:
                left = inorderTraversal(root.left)
                right = inorderTraversal(root.right)
                return left + [root.val] + right
            return []

        return inorderTraversal(root)[k-1]

class IterativeSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
