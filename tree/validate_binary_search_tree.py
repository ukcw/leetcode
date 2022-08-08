# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Correct tree:
                        5
                3               7
            1       4       6       8
        '''
        '''
        Incorrect tree:
                        5
                3               7
            1       6       4       8

        With algorithm:
                                    5 (-inf, +inf)

                    3 (-inf, 5)                   7 (5, +inf)

            1 (-inf, 3)       6 (3, 5)      4 (5, 7)       8 (7, +inf)
        '''
        def validifyBST(root: Optional[TreeNode], flr, ceil) -> bool:
            if not root: return True

            return root.val > flr and root.val < ceil \
                and validifyBST(root.left, flr, root.val) \
                and validifyBST(root.right, root.val, ceil)

        return validifyBST(root, float('-inf'), float('+inf'))
