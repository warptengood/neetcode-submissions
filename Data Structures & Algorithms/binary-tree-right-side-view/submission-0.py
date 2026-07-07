class Solution:
    
    def clearTree(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        root.seen = False
        self.clearTree(root.left)
        self.clearTree(root.right)

    def reveal(self, root: Optional[TreeNode], depth: int, threshold: int) -> int:
        if root is None:
            return depth - 1
        
        if depth > threshold:
            root.seen = True

        right_wing = self.reveal(root.right, depth + 1, threshold)
        threshold = max(threshold, right_wing)

        left_wing = self.reveal(root.left, depth + 1, threshold)
        return max(left_wing, right_wing)

    def get(self, root, ans):
        if root is None:
            return
        if root.seen:
            ans.append(root.val)
        self.get(root.right, ans)
        self.get(root.left, ans)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.clearTree(root)
        self.reveal(root, 0, -1)
        ans = []
        self.get(root, ans)
        return ans