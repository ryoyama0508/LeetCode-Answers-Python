class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        i = 0
        while nums[i] == nums[i+1] and i < len(nums)-1:
            i += 1
            if i == len(nums)-1:
                return 1

        nums = nums[i:]
        diff = nums[1] - nums[0]
        count = 2
        for j in range(1, len(nums)-1):
            newDiff = nums[j+1]-nums[j]
            if (diff < 0 and newDiff > 0) or (diff > 0 and newDiff < 0):
                diff = newDiff
                count += 1
        return count
