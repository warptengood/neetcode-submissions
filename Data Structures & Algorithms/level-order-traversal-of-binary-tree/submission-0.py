# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        res = []

        while (len(q) > 0):
            node, lvl = q.popleft()
            if node is not None:
                if lvl < len(res):
                    res[lvl].append(node.val)
                else:
                    res.append([node.val])
                q.append((node.left, lvl + 1))
                q.append((node.right, lvl + 1))
        return res
