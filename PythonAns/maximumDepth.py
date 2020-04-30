# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depthR = self.maxDepth(root.right)
        depthL = self.maxDepth(root.left)

        if depthL > depthR:
            return depthL + 1
        else:
            return depthR + 1
