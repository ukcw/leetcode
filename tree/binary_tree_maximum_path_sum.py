# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at every node, we have two decisions to make:
        # (1) calculate total sum if we split at this node
        # (2) return maximum sum if no split occurs

        self.maxSum = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            # cut the evaluation early if it's a leaf node OR has no benefit to adding
            if not left and not right:
                self.maxSum = max(self.maxSum, root.val)
                return root.val

            split = root.val + left + right
            leftBranch = left + root.val
            rightBranch = right + root.val

            self.maxSum = max(self.maxSum, split, leftBranch, rightBranch, root.val)

            return max(leftBranch, rightBranch, root.val)

        dfs(root)

        return self.maxSum
