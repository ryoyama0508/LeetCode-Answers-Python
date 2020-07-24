class Solution(object):
    def maximalSquare(self, matrix):
        copy = [[0 for i in range(len(matrix[0]))]for i in range(len(matrix))]
        ret = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == '1':
                    copy[i][j] = min(copy[i-1][j-1], copy[i-1]
                                     [j], copy[i][j-1])+1
                    ret = max(ret, copy[i][j])
        return ret**2

    def maximalSquare1(self, matrix):
        ret = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == '1':
                    ret = max(self.diagonal(matrix, i, j, 0), ret)
        return ret**2

    def diagonal(self, matrix, i, j, long):
        if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
            return long
        right = self.right(matrix, i, j+1, long+1)
        diagonal = self.diagonal(matrix, i+1, j+1, long+1)
        down = self.down(matrix, i+1, j, long+1)
        return min(right, diagonal, down)

    def right(self, matrix, i, j, long):
        if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
            return long
        return self.right(matrix, i, j+1, long+1)

    def down(self, matrix, i, j, long):
        if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
            return long
        return self.down(matrix, i+1, j, long+1)
