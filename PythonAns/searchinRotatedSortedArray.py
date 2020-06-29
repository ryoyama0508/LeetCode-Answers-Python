class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1

        snums = sorted(nums)
        p = nums[0]

        place = self.binarySearch(snums, target, 0, len(nums)-1)
        if place == -1:
            return -1

        rot = self.binarySearch(snums, p, 0, len(nums)-1)
        if rot == 0:
            return place
        ret = place - rot
        if ret < 0:
            return len(nums)+ret

        return ret

    def binarySearch(self, nums, target, start, end):
        if end-start+1 <= 0:
            return -1
        else:
            midpoint = start + (end - start) // 2
            if nums[midpoint] == target:
                return midpoint
            else:
                if target < nums[midpoint]:
                    return self.binarySearch(nums, target, start, midpoint-1)
                else:
                    return self.binarySearch(nums, target, midpoint+1, end)
