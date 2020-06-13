class Solution:
    def maxProfit(self, prices):
        if len(prices) == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        i = 0
        sum = 0
        v, p = prices[0], prices[0]
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i + 1]:
                i += 1
            v = prices[i]
            while i < len(prices)-1 and prices[i] <= prices[i + 1]:
                i += 1
            p = prices[i]

            sum += p - v

        return sum
