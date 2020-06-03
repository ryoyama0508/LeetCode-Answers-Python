class Solution(object):
    def plusOne(self, d):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(d) - 1
        while i > -1:
            if d[i] != 9:
                d[i] = d[i] + 1
                break
            else:
                d[i] = 0
                i -= 1

                if i == -1:
                    d.insert(0, 1)

        return d
