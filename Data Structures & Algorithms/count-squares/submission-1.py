class CountSquares:

    def __init__(self):
        self.points = {}
        self.N = 2000
        self.x = [[] for _ in range(self.N)]

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.points:
            self.points[(point[0], point[1])] = 0
        self.points[(point[0], point[1])] += 1
        self.x[point[0]].append(point[1])

    def count(self, point: List[int]) -> int:
        qx, qy = point
        ans = 0
        for y in self.x[qx]:
            if qy == y:
                continue
            side = abs(qy - y)
            for side in [qy - y, -qy + y]:
                if 0 <= qx + side < self.N:
                    x = qx + side
                    p1 = self.points.get((x, qy), 0)
                    p2 = self.points.get((x, y), 0)
                    ans += p1 * p2
        return ans