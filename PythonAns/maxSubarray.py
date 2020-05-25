class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = prev = nums[0]
        i = 0
        for num in nums:
            if i == 0:
                i += 1
                continue
            prev = max(num, prev + num)
            curr = max(curr, prev)

        return curr
