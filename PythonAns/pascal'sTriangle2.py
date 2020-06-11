class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        return self.recur(rowIndex, 0, [])

    def recur(self, rowIndex, i, prevRow):
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

        if i == rowIndex+1:
            return newRow

        return self.recur(rowIndex, i, newRow)
