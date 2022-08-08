# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree: Optional[TreeNode], subTree: Optional[TreeNode]) -> bool:
            if tree and subTree:
                return tree.val == subTree.val \
            and isSameTree(tree.left, subTree.left) \
            and isSameTree(tree.right, subTree.right)

            return tree is subTree

        if root:
            return isSameTree(root, subRoot) \
            or self.isSubtree(root.left, subRoot) \
            or self.isSubtree(root.right, subRoot)

        return root is subRoot
