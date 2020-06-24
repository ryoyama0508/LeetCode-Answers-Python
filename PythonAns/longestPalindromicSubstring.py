class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        start = end = 0
        for i in range(0, len(s)):
            lenP1 = self.center(s, i, i)
            lenP2 = self.center(s, i, i+1)
            le = max(lenP1, lenP2)
            if le > end - start:
                start = i - ((le - 1)/2)
                end = i + (le / 2)

        return s[start: end + 1]

    def center(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1
