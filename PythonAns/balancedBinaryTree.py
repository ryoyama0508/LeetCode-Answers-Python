# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isTrue, _ = self.recur(root)
        return isTrue

    def recur(self, root):
        if root is None:
            return True, 0

        isTrueL = isTrueR = False
        isTrueL, leftDep = self.recur(root.left)
        isTrueR, rightDep = self.recur(root.right)

        if isTrueL is False or isTrueR is False:
            return False, None

        d = max(rightDep, leftDep)
        s = min(rightDep, leftDep)

        if d - s > 1:
            return False, None
        else:
            return True, d + 1
