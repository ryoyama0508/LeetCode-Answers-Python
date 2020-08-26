import math


class Solution:
    def coinChange(self, coins, amount):
        self.memo = {}
        self.ret = math.inf
        self.dp(coins, amount, 0)

    def dp(self, coins, rest, depth):
        i = 0
        while i < len(coins):
            if rest < 0:
                return
            if rest == 0:
                self.ret = min(self.ret, depth)
            for j in range(len(coins)):
                self.dp(coins, rest - coins[j], depth+1)


obj = Solution()
coins = [1, 2, 5]
print(obj.coinChange(coins, 12))
