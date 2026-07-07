# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        q = deque()
        q.append(root)
        while (len(q) > 0):
            node = q.popleft()
            data.append("N" if node is None else node.val)
            if node is not None:
                q.append(node.left)
                q.append(node.right)
        res = ""
        for i, v in enumerate(data):
            res += (f"{v}," if i != len(data) - 1 else f"{v}")
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        if vals[0] == 'N':
            return None
        q = deque()
        root = TreeNode(vals[0])
        q.append(root)
        index = 1
        while (len(q) > 0):
            node = q.popleft()
            if index < len(vals) and vals[index] != "N":
                node.left = TreeNode(vals[index])
                q.append(node.left)
            index += 1
            if index < len(vals) and vals[index] != "N":
                node.right = TreeNode(vals[index])
                q.append(node.right)
            index += 1
        return root
"""
1, [1]
3, [2, 3]

"""
