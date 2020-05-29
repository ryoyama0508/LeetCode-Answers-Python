class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        ret = 1
        if x < 0:
            ret *= -1

        retStr = ''
        str_ = str(x)
        mark = False
        for i in reversed(str_):
            if (i == '0' and mark is False) or i == '-':
                continue
            retStr += i
            mark = True

        ret *= int(retStr)

        if ret < (-2)**31 or ret > (2**31)-1:
            return 0

        return ret
