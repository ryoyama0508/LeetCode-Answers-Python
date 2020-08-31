class Solution(object):
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (i - j == 0) or (j - i == 1 and s[i] == s[j]) or (dp[i+1][j-1] == 1 and s[i] == s[j]):
                    res += 1
                    dp[i][j] = 1
        return res


obj = Solution()
print(obj.countSubstrings("abc"))
