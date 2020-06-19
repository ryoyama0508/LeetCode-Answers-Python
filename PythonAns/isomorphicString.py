class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in range(0, len(s)):
            if s[i] in dic1:
                if dic1[s[i]] != t[i]:
                    return False
            if t[i] in dic2:
                if dic2[t[i]] != s[i]:
                    return False

            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]

        return True
