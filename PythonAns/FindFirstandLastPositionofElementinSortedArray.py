class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.bs(nums, target, 0, len(nums)-1)
        print(idx)
        if idx == -1:
            return [-1, -1]

        s = 0
        if idx != 0:
            while idx > 0 and nums[idx] == nums[idx - 1]:
                idx -= 1
            s = idx

        e = len(nums)-1
        if idx != len(nums)-1:
            while idx < len(nums)-1 and nums[idx] == nums[idx+1]:
                idx += 1
            e = idx
        return [s, e]

    def bs(self, nums, target, start, end):
        if end-start+1 <= 0:
            return -1
        else:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.bs(nums, target, start, mid-1)
            else:
                return self.bs(nums, target, mid+1, end)
