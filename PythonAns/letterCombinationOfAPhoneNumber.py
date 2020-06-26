class Solution(object):
    def letterCombinations(self, d):
        """
        :type d: str
        :rtype: List[str]
        """
        chrs = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
            "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        return self.backTracking(d, 0, "", [], chrs)

    def backTracking(self, d, i, oneSet, ret, chrs):
        if i == len(d):
            ret.append(oneSet)
            return

        chrslist = chrs[int(d[i])-2]
        for j in range(0, len(chrslist)):
            oneSet += chrslist[j]
            self.backTracking(d, i+1, oneSet, ret, chrs)
            oneSet = oneSet[:-1]

        return ret
