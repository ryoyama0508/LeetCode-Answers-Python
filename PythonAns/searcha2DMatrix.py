class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = l + (r-l)//2
            row, col = mid / len(matrix[0]), mid % len(matrix[0])
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False
