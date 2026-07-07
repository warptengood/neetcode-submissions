# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {node:i for i, node in enumerate(inorder)}
        stack = []

        root = TreeNode(preorder[0])
        stack.append((root, 0, len(inorder) - 1))

        for i in range(1, len(preorder)):
            new_node = TreeNode(preorder[i])
            cur_pos_in = mapping[preorder[i]]
            while cur_pos_in < stack[-1][1] or stack[-1][2] < cur_pos_in:
                stack.pop()
            parent = stack[-1][0]
            lb = stack[-1][1]
            rb = stack[-1][2]

            if lb <= cur_pos_in < mapping[parent.val]:
                parent.left = new_node
                stack.append((new_node, lb, mapping[parent.val] - 1))
            elif mapping[parent.val] < cur_pos_in <= rb:
                parent.right = new_node
                stack.append((new_node, mapping[parent.val] + 1, rb))
        
        return root