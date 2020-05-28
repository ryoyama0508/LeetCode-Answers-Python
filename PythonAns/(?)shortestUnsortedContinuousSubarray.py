class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = b = leftI = rightI = 0
        for i, num in enumerate(nums):
            if nums[i + 1] < num:
                s = nums[i+1]
                b = num
                leftI = i+1
                rightI = i + 2
                break

        if s == 0 and b == 0:
            return []

        right = 0
        while rightI < len(nums):
            if nums[rightI] < b:
                right = rightI
            else:
                b = nums[rightI]
            rightI += 1
            print("b", b)
            print(rightI)

        left = 0
        while leftI > -1:
            if nums[leftI] > s:
                left = leftI
            else:
                s = nums[leftI]
            leftI -= 1
            print("s", s)
            print(leftI)

        print(left, right)
