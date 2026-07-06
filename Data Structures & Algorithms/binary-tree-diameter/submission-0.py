# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if root is None:
            return -1, -1
        left_depth, left_ans = self.solve(root.left)
        right_depth, right_ans = self.solve(root.right)
        current_depth = max(left_depth, right_depth) + 1
        return current_depth, max(left_ans, right_ans, left_depth + right_depth + 2, current_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, ans = self.solve(root)
        return ans