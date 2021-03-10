class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        def helper(nums):
            if not len(nums):
                return [None]
            ret = []
            for i in range(len(nums)):
                for l in helper(nums[:i]):
                    for r in helper(nums[i + 1 :]):
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        ret.append(root)

            return ret

        return helper([i for i in range(1, n + 1)])
