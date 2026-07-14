class Solution:

    def check(self, pos):
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                if pos[i][0] == pos[j][0] or pos[i][1] == pos[j][1]:
                    return False
                if abs(pos[i][0] - pos[j][0]) == abs(pos[i][1] - pos[j][1]):
                    return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        cur = []
        ans = []
        def rec(pos, q):
            if q == n + 1:
                ans.append(cur.copy())
                return
            if pos == n * n:
                return

            x, y = pos // n, pos % n
            cur.append((x, y))
            
            if self.check(cur):
                rec(pos + 1, q + 1)
            cur.pop()
            rec(pos + 1, q)
            
        rec(0, 1)
        output = []
        for pos in ans:
            b = [['.'] * n for _ in range(n)]
            for x, y in pos:
                b[x][y] = 'Q'
            b = ["".join(row) for row in b]
            output.append(b)
        return output