class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeroes = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                zeroes += 1
                nums.pop(i)
            else:
                i += 1

        l = 0
        while l < zeroes:
            nums.append(0)
            l += 1
