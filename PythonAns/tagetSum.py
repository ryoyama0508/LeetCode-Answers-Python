class Solution(object):
    def findTargetSumWays(self, nums, S):
        memoList = [dict() for i in range(0, len(nums)-1)]

        def dp(nums, S, sum, idx, memoList):
            addSum = sum + nums[idx]
            subSum = sum - nums[idx]
            if idx == len(nums)-1:
                c = 0
                if addSum == S:
                    c += 1
                if subSum == S:
                    c += 1
                return c

            addSumCount, subSumCount = 0, 0
            if addSum in memoList[idx]:
                addSumCount = memoList[idx][addSum]
            else:
                addSumCount = dp(nums, S, addSum, idx+1, memoList)

            if subSum in memoList[idx]:
                subSumCount = memoList[idx][subSum]
            else:
                subSumCount = dp(nums, S, subSum, idx+1, memoList)
            memoList[idx][addSum] = addSumCount
            memoList[idx][subSum] = subSumCount
            return addSumCount + subSumCount
        return dp(nums, S, 0, 0, memoList)
