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
        self.ret = []
        nums.sort()  # point
        # sorting and skip method can skip the same subtree of the left next tree.
        # you can see the doc here
        self.helper2(nums, [])
        return self.ret

    def helper2(self, choices, pattern):
        if not len(choices):
            self.ret.append(pattern)
            return

        for i in range(len(choices)):
            if i > 0 and choices[i] == choices[i - 1]:
                continue
            self.helper(choices[:i] + choices[i + 1 :], pattern + [choices[i]])
