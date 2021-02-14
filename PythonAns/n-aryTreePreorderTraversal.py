"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root):
        if root is None:
            return []
        self.ret = [root.val]
        for child in root.children:
            self.traversal(child)
        return self.ret

    def traversal(self, root):
        if root is None:
            return
        self.ret.append(root.val)
        for child in root.children:
            self.traversal(child)