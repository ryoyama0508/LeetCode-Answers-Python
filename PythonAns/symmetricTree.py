# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if len(self) % 2 != 0:
            return False

        else:
            return True


nums = [2, 3, 4, 4, 2]
i = Solution()
i.isSymmetric(nums)
