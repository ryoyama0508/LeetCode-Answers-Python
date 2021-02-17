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

    def lowestCommonAncestor2(self, root, p, q):
        self.isPorQ(root, p, q)
        return self.ret

    def isPorQ(self, root, p, q):
        if root is None:
            return False

        l = self.isPorQ(root.left, p, q)
        r = self.isPorQ(root.right, p, q)
        if l and r:
            self.ret = root
            return False
        elif l or r:
            if root.val == p.val or root.val == q.val:
                self.ret = root
                return False
            else:
                return True
        else:
            if root.val == p.val or root.val == q.val:
                return True
            else:
                return False