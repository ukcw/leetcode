# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(0, root)])
        levelOrderList = []

        while queue:
            depth, node = queue.popleft()
            if node:
                if len(levelOrderList) > depth:
                    levelOrderList[depth].append(node.val)
                if len(levelOrderList) <= depth:
                    levelOrderList.append([node.val])
                queue.append((1 + depth, node.left))
                queue.append((1 + depth, node.right))
        return levelOrderList

