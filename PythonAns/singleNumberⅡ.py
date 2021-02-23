class Solution:
    def singleNumber(self, nums):
        bit_digit = [0] * 32

        for num in nums:
            for i in range(32):
                if (num >> i & 1) != 0:  # bit move
                    bit_digit[i] += 1  # check bit is 1

        # python used 2's conplement inside but not show on format
        ret = 0
        for j in range(32):
            if bit_digit[j] % 3 == 1:
                if j == 31:
                    print("{0:b}".format(ret))
                    print(ret)
                    ret |= 1 << j
                    print("{0:b}".format(ret))
                    print(ret)
                    ret = -((1 << 31) - ret)
                else:
                    ret |= 1 << j

        return ret


obj = Solution()
obj.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2])
