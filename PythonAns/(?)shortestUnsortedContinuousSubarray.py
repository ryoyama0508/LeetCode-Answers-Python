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

    def findUnsortedSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        print(is_same)
        print(is_same.index(False))
        print(is_same[::-1].index(False))
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
