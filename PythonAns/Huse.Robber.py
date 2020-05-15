class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previousTop = top = 0
        for num in nums:
            # topWithoutNowLast represents the biggest nums
            # without thinking newest num and last num
            topWithoutNowLast = previousTop

            previousTop = top  # previousTop represents biggest nums

            # Here we just plug into the formula
            # this formula compare the sum of
            # the newest node + topWithoutNowLast and 2nd biggest nums
            top = max(num + topWithoutNowLast, previousTop)
        return top
