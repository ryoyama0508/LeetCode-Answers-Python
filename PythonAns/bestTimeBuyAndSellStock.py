class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minPri, maxPro = prices[0], 0
        for i in range(1, len(prices)):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i]-minPri)
        return maxPro
