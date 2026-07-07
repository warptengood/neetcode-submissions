# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def pop(self, root):
        if root is None:
            return 0
        lsz = self.pop(root.left)
        rsz = self.pop(root.right)
        sz = lsz + rsz + 1
        root.size = sz
        return sz

    def get(self, root, k):
        lsz = 0 if root.left is None else root.left.size
        if lsz + 1 == k:
            return root.val
        if k < lsz + 1:
            return self.get(root.left, k)
        else:
            return self.get(root.right, k - lsz - 1) 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.pop(root)
        return self.get(root, k)