# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        ret = self.rec(root, 1)
        return ret

    def rec(self, root, c):
        if root is None:
            return None

        leftC = self.rec(root.left, c+1)
        rightC = self.rec(root.right, c+1)

        if leftC != None and rightC != None:
            s = min(leftC, rightC)
        else:
            if leftC == None and rightC != None:
                return rightC
            elif leftC != None and rightC == None:
                return leftC
            elif leftC == None and rightC == None:
                return c

        return s
