class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        return self.recur(numRows, 0, [], [])

    def recur(self, numRows, i, prevRow, pascal):
        i += 1
        newRow = [0] * i
        idx = 0
        j = 0
        while idx < len(newRow):
            if idx == 0 or idx == len(newRow)-1:
                newRow[idx] = 1
            else:
                newRow[idx] = prevRow[j] + prevRow[j + 1]
                j += 1
            idx += 1

        pascal.append(newRow)

        if i == numRows:
            return pascal

        return self.recur(numRows, i, newRow, pascal)
