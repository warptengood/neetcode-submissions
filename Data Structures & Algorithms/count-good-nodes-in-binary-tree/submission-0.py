# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(node, max_val):
            if node is None:
                return 0
            is_good = max_val <= node.val
            max_val = max(max_val, node.val)
            return is_good + solve(node.left, max_val) + solve(node.right, max_val) 
        return solve(root, -1000)