class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        is_row_white = is_col_white = 0
        for i in range(n):
            if matrix[i][0] == 0:
                is_col_white = 1
                break

        for j in range(m):
            if matrix[0][j] == 0:
                is_row_white = 1
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_col_white:
            for i in range(n):
                matrix[i][0] = 0

        if is_row_white:
            for j in range(m):
                matrix[0][j] = 0