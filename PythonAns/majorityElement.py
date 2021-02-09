class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1

        for i, v in dic.items():
            if v > (len(nums)/2):
                return i

# Follow-up: Could you solve the problem in linear time and in O(1) space?
