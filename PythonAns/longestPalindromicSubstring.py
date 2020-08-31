class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            print(i, "idx")
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            print(tmp)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            print(tmp)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        print(l, r, "helper")
        return s[l+1:r]


obj = Solution()
print(obj.longestPalindrome("cbbd"))


class Solution2:
    def longestPalindrome2(self, s: str) -> str:
        dp = [[0 for i in range(len(s))] for i in range(len(s))]
        ret = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if len(s)-j < len(ret):
                    break
                if (i - j == 0) or (j - i == 1 and s[i] == s[j]) or (dp[i+1][j-1] == 1 and s[i] == s[j]):
                    feas_ans = s[i:j+1]
                    if len(feas_ans) > len(ret):
                        ret = s[i:j+1]
                    dp[i][j] = 1
        return ret
