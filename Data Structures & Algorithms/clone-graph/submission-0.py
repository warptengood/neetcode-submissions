"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        vis = {}
        def dfs(node, copy_node):
            if node is None:
                return
            vis[copy_node.val] = copy_node
            for n in node.neighbors:
                if n.val in vis:
                    copy_node.neighbors.append(vis[n.val])
                else:
                    new_node = Node(n.val)
                    copy_node.neighbors.append(new_node)
                    dfs(n, new_node)
        root = None
        if node is not None:
            root = Node(node.val)
            dfs(node, root)
        return root

