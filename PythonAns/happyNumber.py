class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while n:
            if 1 in dic:
                return True
            if n in dic:
                return False

            dic[n] = 0
            temp = 0
            while n > 0:
                temp += (n % 10)**2
                n //= 10
            n = temp
