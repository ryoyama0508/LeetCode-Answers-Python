# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not inorder:
            return
        i = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[i])
        linorder = inorder[:i]
        rinorder = inorder[i+1:]
        root.left = self.buildTree(preorder, linorder)
        root.right = self.buildTree(preorder, rinorder)
        return root
