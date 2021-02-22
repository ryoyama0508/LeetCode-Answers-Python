class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ssum, tsum = 0, 0
        for i in range(len(s)):
            ssum += ord(s[i])
            tsum += ord(t[i])
        tsum += ord(t[-1])
        return chr(tsum - ssum)