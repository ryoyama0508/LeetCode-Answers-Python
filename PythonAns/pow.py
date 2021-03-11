class Solution:
    def myPow(self, x: float, n: int) -> float:  # mine
        memo = {}

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                memo[n] = x
                return x

            if n in memo:
                return memo[n]
            if n % 2 != 0:
                ret = x * helper(x, n - 1)
            else:
                ret = helper(x, n // 2) * helper(x, n // 2)

            memo[n] = ret
            return ret

        arg = n
        if n < 0:
            arg = -n
        ret = helper(x, arg)
        if n < 0:
            ret = 1 / ret

        return ret