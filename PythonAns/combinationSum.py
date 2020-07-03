class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, 0, [], res)
        return res

    def dfs(self, candidates, target, sumSF, idx, one, ret):
        if sumSF > target:
            return one[:-1]
        if sumSF == target:
            ret.append(one)
            return one[:-1]
        for i in range(idx, len(candidates)):
            sumSF += candidates[i]
            one.append(candidates[i])
            one = self.dfs(candidates, target, sumSF, i, one, ret)
            sumSF -= candidates[i]
        one = one[:-1]

        return one

    def dfs2(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs2(nums, target-nums[i], i, path+[nums[i]], res)
