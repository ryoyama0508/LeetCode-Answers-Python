class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                print(start, dic[ch] + 1)
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s)-start)

    def TLElengthOfLongestSubstring(self, s):  # Time Limit Exceeded
        """
        :type s: str
        :rtype: int
        """
        return self.recur(s, 0, 0)

    def recur(self, s, i, m):
        dic = {}
        now = 0
        for j in range(i, len(s)):
            if s[j] in dic:
                m = max(m, now)
                return self.recur(s, dic[s[j]]+1, m)
            dic[s[j]] = j
            now += 1

        return max(m, now)
