class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = 0
        for num in nums:
            res ^= num
            print(res)

        return res

    def singleNumber2(self, nums):
        dic = {}
        for num in nums:  # dictionary doesnt have the same key
            # get() takes value whose key applys the first arg
            dic[num] = dic.get(num, 0)+1
            print(dic)
        for key, val in dic.items():  # items take key and val from dictionary by using for
            if val == 1:
                return key

    def singleNumberBruteForce(self, nums):  # timelimit exceeded
        """
        :type nums: List[int]
        :rtype: int
        """
        list = []
        for n in nums:
            if n in list:
                list.remove(n)  # here is the problem
            else:
                list.append(n)
        return list[0]


nums = [2, 3, 4, 4, 2]
i = Solution()
i.singleNumber2(nums)
