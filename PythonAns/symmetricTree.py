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
        if root is None:
            return True

        return self.checkNords(root.left, root.right)

    def checkNords(self, l, r):
        if l is None:
            if r is None:
                return True
            else:
                return False
        if r is None:
            if l is None:
                return True
            else:
                return False

        if r.right is None and r.left is None and l.right is None and l.left is None:
            if r.val == l.val:
                return True
            return False

        return l.val == r.val and self.checkNords(l.left, r.right) and self.checkNords(l.right, r.left)


nums = [2, 3, 4, 4, 2]
i = Solution()
i.isSymmetric(nums)
