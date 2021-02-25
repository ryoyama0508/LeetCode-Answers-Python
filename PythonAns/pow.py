class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            tmp = -n
        else:
            tmp = n

        ret = x
        for i in range(tmp - 1):
            ret = ret * x

        print(x)
        if n < 0:
            return 1 / ret
        return ret