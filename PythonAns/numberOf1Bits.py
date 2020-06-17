class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for _ in range(0, 32):
            ret += n % 2
            n = n//2
        return ret
