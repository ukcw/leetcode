"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.nodes = {}

        def iterClone(node):
            if node.val not in self.nodes:
                self.nodes[node.val] = Node(node.val)

                for idx, n in enumerate(node.neighbors):
                    self.nodes[node.val].neighbors.append(iterClone(n))

                return self.nodes[node.val]
            else:
                return self.nodes[node.val]

        return iterClone(node) if node else node
