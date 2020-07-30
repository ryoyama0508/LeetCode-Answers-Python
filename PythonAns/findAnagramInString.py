from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        ret = []
        l = len(p)
        windowp = Counter(p)
        windows = Counter(s[:l-1])
        i = 0
        while i+l <= len(s):
            windows[s[i+l-1]] += 1
            if windows == windowp:
                ret.append(i)
            windows[s[i]] -= 1
            if windows[s[i]] == 0:
                del windows[s[i]]
            i += 1
        return ret
