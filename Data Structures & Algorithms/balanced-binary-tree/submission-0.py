# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):
        if root is None:
            return -1, True
        lh, lans = self.solve(root.left)
        rh, rans = self.solve(root.right)

        return max(lh, rh) + 1, lans and rans and abs(lh - rh) <= 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, ans = self.solve(root)
        return ans
        