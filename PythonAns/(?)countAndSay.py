class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        startNum = [1, 1, 0]
        return self.recur(startNum, 2, n, 0, 0)

    def recur(self, nums, now, goal, i, j):
        newNums = [0] * (2 * len(nums))
        count = 1

        while True:
            if nums[i + 1] == 0 or i+1 == len(nums):
                newNums[j] = count
                newNums[j + 1] = nums[i]
                break
            if nums[i] != nums[i + 1]:
                newNums[j] = count
                newNums[j + 1] = nums[i]
                j += 2
                count = 1
            else:
                count += 1
            i += 1
        now += 1

        if now == goal:
            ret = ''.join([str(n) for n in newNums if n != 0])
            return ret

        return self.recur(newNums, now, goal, 0, 0)
