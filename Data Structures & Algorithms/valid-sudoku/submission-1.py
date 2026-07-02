class Solution:
    
    def check(self, s: list[str]) -> bool:
        met = set()
        for c in s:
            if c in met and c != '.':
                return False
            met.add(c)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row = self.check(board[i][:])
            col = self.check([line[i] for line in board])
            if not row or not col:
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                st_i = i * 3
                st_j = j * 3
                flat = []
                for k in range(st_i, st_i + 3):
                    flat.extend(board[k][st_j: st_j + 3])
                if not self.check(flat):
                    return False
        return True

        