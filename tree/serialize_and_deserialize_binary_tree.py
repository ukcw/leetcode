# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BFSCodec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                output.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            if not node:
                output.append('#')

        return ' '.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def createNode(val):
            return None if val == '#' else TreeNode(int(val))

        data = collections.deque(data.split())
        root = createNode(data.popleft())
        queue = collections.deque([root])

        while queue:
            curr = queue.popleft()
            if curr:
                curr.left = createNode(data.popleft())
                curr.right = createNode(data.popleft())
                queue.append(curr.left)
                queue.append(curr.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
