class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, int(round(len(res)**(0.5)+1))):
            if res[i]:
                for j in range(i*2, len(res), i):
                    res[j] = False

        return sum(res)
