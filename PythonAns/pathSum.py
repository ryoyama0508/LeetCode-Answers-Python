# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.recur(root, 0, sum)

    def recur(self, root, s, sum):
        if root is None:
            return None

        s += root.val

        isTrueL = self.recur(root.left, s, sum)
        isTrueR = self.recur(root.right, s, sum)

        if isTrueL is None and isTrueR is None:
            if s == sum:
                return True
            else:
                return False

        ret = False
        if root.right is None and root.left:
            ret = isTrueL
        elif root.right and root.left is None:
            ret = isTrueR
        else:
            if isTrueL == True or isTrueR == True:
                ret = True

        return ret
