class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)
        for char in reversed(s):
            if char == " ":
                s = s[:i-1]
            else:
                break
            i -= 1

        count = 0
        idx = len(s)
        while idx > 0:
            if s[idx - 1] == " ":
                return count
            else:
                idx -= 1
                count += 1
        return count
