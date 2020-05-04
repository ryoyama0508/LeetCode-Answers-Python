class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num] = i


nums = [3, 2, 4]
i = Solution()
ans1, ans2 = i.twoSum(nums, 6)
print(ans1, ans2)
