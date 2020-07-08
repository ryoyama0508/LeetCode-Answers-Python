class Solution(object):
    def subsets(self, nums):
        ret = []
        self.back(nums, [], ret)
        return ret

    def back(self, nums, one, ret):
        ret.append(one)
        if len(nums) == 0:
            return

        i = 0
        while i < len(nums):
            newOne = one + [nums[0]]
            if len(nums) > 0:
                nums = nums[1:]
            self.back(nums, newOne, ret)
