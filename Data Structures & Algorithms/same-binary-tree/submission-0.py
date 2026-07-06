# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            lans = self.isSameTree(p.left, q.left)
            rans = self.isSameTree(p.right, q.right)
            return lans and rans and (p.val == q.val)
        return False