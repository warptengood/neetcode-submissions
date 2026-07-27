class Solution:

    def transpose(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    def flip_x(self, matrix):
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m // 2 + (m % 2 == 1)):
                matrix[i][j], matrix[i][m - j - 1] = matrix[i][m - j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.flip_x(matrix)