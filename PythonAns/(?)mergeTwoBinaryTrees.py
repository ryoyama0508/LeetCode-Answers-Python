# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2:
            if t2.right is None:
                if t2.left is None:
                    return t2
                else:
                    l = self.mergeTrees(None, t2.left)
                    t3Node = TreeNode(0)
                    t3Node.val = t2.val
                    t3Node.left = l
                    return t3Node

        if t1 and t1.right is None and t1.left and t2 is None:
            return t1
        if t1.right is None and t1.left is None and t2.right is None and t2.left is None:
            t3endNode = TreeNode(0)
            t3endNode.val = t1.val + t2.val
            return t3endNode

        l = self.mergeTrees(t1.left, t2.left)
        r = self.mergeTrees(t1.right, t2.right)

        t3Node = TreeNode(0)
        t3Node.val = t1.val + t2.val
        t3Node.right = r
        t3Node.left = l
        return t3Node
