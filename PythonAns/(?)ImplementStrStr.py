class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1, l2 = len(haystack), len(needle)
        for i in range(l1 - l2 + 1):
            if needle == haystack[i : i + l2]:
                return i
        return -1


# test
