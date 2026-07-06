class Solution:

    def flaten(self, root: Optional[TreeNode], flat: list[int]):
        if root is None:
            return
        flat.append(root.val + 200)
        self.flaten(root.left, flat)
        self.flaten(root.right, flat)

    def find_subtree_r(self, root, subtree_r, cur_id) -> int:
        if root is None:
            return 0
        lsz = self.find_subtree_r(root.left, subtree_r, cur_id + 1)
        rsz = self.find_subtree_r(root.right, subtree_r, cur_id + lsz + 1)
        subtree_r[cur_id] = cur_id + lsz + rsz
        return lsz + rsz + 1


    def add(self, a: int, b: int, mod: int) -> int:
        return ((a % mod) + (b % mod)) % mod
    
    def mult(self, a: int, b: int, mod: int) -> int:
        return ((a % mod) * (b % mod)) % mod
    
    def sub(self, a: int, b: int, mod: int) -> int:
        return (a - b + mod) % mod

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flat_root, flat_subroot = [], []
        self.flaten(root, flat_root)
        self.flaten(subRoot, flat_subroot)
        mod = 1000000007
        p = 31
        n = len(flat_root)

        subtree_r = [0] * n
        self.find_subtree_r(root, subtree_r, 0)
        
        subroot_hash = 0
        for i, val in enumerate(flat_subroot):
            subroot_hash = self.add(subroot_hash, self.mult(val, p**(n - i - 1), mod), mod)

        pol = []

        for i, val in enumerate(flat_root):
            pol.append(self.add(self.mult(val, p**(n - i - 1), mod), 0 if i == 0 else pol[-1], mod))
        
        for i in range(n):
            pl = 0 if i == 0 else pol[i - 1]
            pr = pol[subtree_r[i]]
            if self.mult(self.sub(pr, pl, mod), p**i, mod) == subroot_hash:
                return True 
        return False 