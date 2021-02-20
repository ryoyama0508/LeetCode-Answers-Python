class Solution:
    def permute(self, nums):
        self.ret = []
        self.helper(nums, [])
        return self.ret

    def helper(self, choices, pattern):
        if not len(choices):
            self.ret.append(pattern)
            return

        for i in range(len(choices)):
            self.helper(choices[:i] + choices[i + 1 :], pattern + [choices[i]])
