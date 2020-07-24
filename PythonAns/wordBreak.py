class Solution(object):
    def wordBreak(self, s, wordDict):
        ch = [False] * (len(s)+1)
        ch[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if ch[j] and s[j:i] in wordDict:
                    ch[i] = True
                    break
        return ch[-1]
