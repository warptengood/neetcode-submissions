class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        penalty = [0, 0, 0, 0]
        dst = [m, n, -1, -1]
        x, y = 0, 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        turn = 0
        res = []
        while True:
            if len(res) > 0:
                res.pop()
            steps = abs(dst[turn] - (y if turn % 2 == 0 else x)) - penalty[turn]
            # print(f"Current state: {res}")
            # print(f"Current turn: {move[turn]}")
            # print(f"Num steps {steps}")
            # print(f"Current pos: {x}, {y}")
            # print(f"Penalty {penalty[turn]}")
            # print()
            for iteration in range(steps):
                res.append(matrix[x][y])
                if iteration < steps - 1:
                    x += move[turn][0]
                    y += move[turn][1]
            penalty[(turn + 3) % 4] += 1
            turn = (turn + 1) % 4

            if not (0 <= x + move[turn][0] * (penalty[turn] + 1) < n and 0 <= y + move[turn][1] * (penalty[turn] + 1) < m):
                break
        # print(f"Current state: {res}")
        # print(f"Current turn: {move[turn]}")
        # print(f"Num steps {steps}")
        # print(f"Current pos: {x}, {y}")
        # print(f"Penalty {penalty[turn]}")
        # print()
        return res