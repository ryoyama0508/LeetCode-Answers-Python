# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        if root == p or root == q:
            return root

        retL = self.lowestCommonAncestor(root.left, p, q)
        retR = self.lowestCommonAncestor(root.right, p, q)

        if not retL and not retR:
            return
        elif retL and not retR:
            return retL
        elif not retL and retR:
            return retR
        else:
            return root

        # what is the actual goal?? the goal is return node!!!
