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
