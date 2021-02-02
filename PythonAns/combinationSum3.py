class Solution:
    def combinationSum3(self, k, n):
        '''
        k is the number of subsets
        and n is the total sum
        backtracing
        '''
        nums = []
        nums = [i for i in range(1, 10)]
        self.ret = []
        print(nums)
        self.back(k, n, nums, 0, [])
        return self.ret

    def back(self, k, n, nums, idx, one_set):
        print(one_set)
        if len(one_set) > k:
            return
        if sum(one_set) == n and len(one_set) == k:
            self.ret.append(one_set)
            return
        for i in range(idx, len(nums)):
            self.back(k, n, nums, i+1, one_set+[nums[i]])


obj = Solution()
print(obj.combinationSum3(3, 15))
