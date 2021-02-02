class Solution:
    def mysetZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        be straight forward, simple
        """
        i_and_j_sets = []

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    i_and_j_sets.append([i, j])

        print(i_and_j_sets)

        for i_and_j in i_and_j_sets:
            print(i_and_j)
            for j in range(0, len(matrix[0])):
                matrix[i_and_j[0]][j] = 0
            for i in range(0, len(matrix)):
                matrix[i][i_and_j[1]] = 0

    def setZeroes(self, matrix):
        """
        use set instead of using list cuz that make O(mn)-> O(m + n)
        """
        column_set, row_set = set(), set()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    column_set.add(i)
                    row_set.add(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in column_set or j in row_set:
                    matrix[i][j] = 0
        print(matrix)


obj = Solution()
mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
obj.setZeroes(mat)
