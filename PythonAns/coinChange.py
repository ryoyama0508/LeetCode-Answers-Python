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


class Solution2(object):
    def __init__(self):
        self.memo = {0: 0}

    def coinChange(self, coins, amount):
        coins.sort()
        minCoins = self.dp(coins, amount)
        return minCoins if minCoins != float('inf') else -1

    def dp(self, coins, rest):
        print(rest)
        if rest in self.memo:
            return self.memo[rest]

        minDepth = float('inf')
        for coin in coins:
            if rest - coin < 0:
                break
            d = self.dp(coins, rest - coin)
            minDepth = min(minDepth, d+1)

        self.memo[rest] = minDepth
        print(minDepth, rest)
        return minDepth


obj2 = Solution2()
coins = [1, 2, 5]
print(obj2.coinChange(coins, 12))
