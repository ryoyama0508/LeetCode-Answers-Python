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


class AnotherSolution(object):
    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        l = 0
        r = len(nums)-1

        while l <= r:
            p = (l+r)/2

            if nums[l] == target:
                return l
            if nums[p] == target:
                return p
            if nums[r] == target:
                return r

            # array sorted
            if nums[l] < nums[r]:
                # binary search

                # check target is in range
                if target < nums[l] or nums[r] < target:
                    return -1

                if target < nums[p]:
                    r = p-1
                else:
                    l = p+1

            # array not sorted
            else:
                # the left half is sorted
                if nums[l] < nums[p]:
                    # the left half is sorted and target in it, search left.
                    if nums[l] < target and target < nums[p]:
                        r = p-1
                    else:
                        l = p+1

                # the right half is sorted
                else:
                    # the right half is sorted and target in it, search right.
                    if nums[p] < target and target < nums[r]:
                        l = p+1
                    else:
                        r = p-1
        return -1
