class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        cont = nums[0]
        best = nums[0]
        for num in nums[1:]:
            cont = max(num, cont + num)

            # still cannot understand
            best = max(best, cont)
        return best

    def maxSubArray2(self, nums):
        sum_list = [0] * len(nums)
        for i in range(len(nums)):
            sum_list[i] = max(sum_list[i-1] + nums[i], nums[i])

        return max(sum_list)
