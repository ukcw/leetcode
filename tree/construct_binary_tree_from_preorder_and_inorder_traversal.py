# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder
        [3,9,20,15,7]
        -- remove 3 from the array
        [9,20,15,7]
        -- remove 9 from the array
        [20,15,7]
        -- remove 20 from the array
        [15,7]
        -- remove 15 from the array

        inorder
        [9,3,15,20,7]
        -- find index of 3
        -- split array into left-side of 3 and right-side of 3
        [9] [15,20,7]
        -- find index of 9 in the left array
        -- split array into left-side of 9 and right-side of 9 (there is nothing left in inorder list)
        -- find index of 20 in the right array
        -- split array into left-side of 20 and right-side of 20
        [15] [7]
        -- find index of 15 in the left array
        -- split array into left-side of 15 and right-side of 15 (there is nothing left in inorder list)
        -- find index of 7 in the left array
        -- split array into left-side of 7 and right-side of 7 (there is nothing left in inorder list)
        '''
        if inorder:
            root = TreeNode(preorder.pop(0))

            inorderIdx = inorder.index(root.val)

            root.left = self.buildTree(preorder, inorder[:inorderIdx])
            root.right = self.buildTree(preorder, inorder[inorderIdx+1:])

            return root
