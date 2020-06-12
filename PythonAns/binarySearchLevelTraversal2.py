# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root):
        ori = []
        return self.recur(root, 1, ori)

    def recur(self, root, lev, ori):
        if root is None:
            return None

        if len(ori) < lev:
            ori.insert(-lev, [])
        ori[-lev].append(root.val)
        retL = self.recur(root.left, lev + 1, ori)
        retR = self.recur(root.right, lev + 1, ori)

        if retL is None and retR is None:
            if lev == 1:
                return ori
            else:
                return None
