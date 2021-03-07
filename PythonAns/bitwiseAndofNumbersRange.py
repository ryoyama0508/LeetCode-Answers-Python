class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        for i in range(32):
            if 2 ** (i + 1) <= left and 2 ** (i + 1) <= right:
                continue
            if 2 ** i <= left:
                if 2 ** (i + 1) <= right:
                    return 0
                else:
                    ret = left
                    for j in range(left, right + 1):
                        ret &= j
                    return ret
            else:
                if 2 ** 1 <= right:
                    return 0
                else:
                    ret = left
                    for j in range(left, right + 1):
                        ret &= j
                    return ret

    # https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation