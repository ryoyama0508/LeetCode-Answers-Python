class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        temp = nums[-k:]
        nums[:] = nums[:-k]
        nums[:] = temp + nums
