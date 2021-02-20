class Solution:
    def permuteUnique(self, nums):
        self.dict = {}
        self.helper(nums, [])
        ret = []
        for key in self.dict:
            ret.append(key)
        return ret

    def helper(self, choices, pattern):
        if not len(choices):
            if not tuple(pattern) in self.dict:
                self.dict[tuple(pattern)] = ""
            return

        for i in range(len(choices)):
            self.helper(choices[:i] + choices[i + 1 :], pattern + [choices[i]])

    def permuteUnique2(self, nums):
        self.dict = {}
        self.helper(nums, [])
        ret = []
        for key in self.dict:
            ret.append(key)
        return ret

    def helper2(self, choices, pattern):
        if not len(choices):
            if not tuple(pattern) in self.dict:
                self.dict[tuple(pattern)] = ""
            return

        for i in range(len(choices)):
            self.helper(choices[:i] + choices[i + 1 :], pattern + [choices[i]])
