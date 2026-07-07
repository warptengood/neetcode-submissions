# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root):
        if root is None:
            # ans, cont_max_path
            return int(-1e9), 0
        
        left = self.rec(root.left)
        right = self.rec(root.right)

        return max(left[0], right[0], root.val + max(left[1], right[1]), root.val + left[1] + right[1], root.val), max(root.val + max(left[1], right[1]), root.val)



    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans, _ = self.rec(root)
        return ans