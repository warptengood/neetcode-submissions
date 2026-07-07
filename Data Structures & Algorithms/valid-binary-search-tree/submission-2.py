# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rec(self, root):
        min_val, max_val = root.val, root.val
        
        if root.left is not None:
            lans, lmin, lmax = self.rec(root.left)
            if not lans:
                return False, -1, -1
            if lmax >= root.val:
                return False, -1, -1
            min_val = min(min_val, lmin)
            max_val = max(max_val, lmax)
        
        if root.right is not None:
            rans, rmin, rmax = self.rec(root.right)
            if not rans:
                return False, -1, -1
            if rmin <= root.val:
                return False, -1, -1
            min_val = min(min_val, rmin)
            max_val = max(max_val, rmax)
        
        return True, min_val, max_val



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        ans, _, _ = self.rec(root)
        return ans