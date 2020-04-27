class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        for i in range(i, len(nums)):
            for j in range(j, len(nums)):
                if nums[i]+nums[j] == target:
                    return i, j
                else:
                    j += 1
            i += 1
            j = i+1


nums = [3, 2, 4]
i = Solution()
ans1, ans2 = i.twoSum(nums, 6)
print(ans1, ans2)
