class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        if x < 999999 and x >= 10000:
            n = 100
        elif x < 99999999 and x >= 1000000:
            n = 1000
        elif x >= 100000000:
            n = 10000
        while True:
            if n ** 2 > x:
                return n - 1
            n += 1
