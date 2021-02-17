# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nodes = []
        for i in range(1, n + 1):
            nodes.append(i)
        self.trees = []
        for i in range(len(nodes)):
            root = TreeNode(nodes[i])

            self.generateTree(nodes[:i], root, root)
            self.generateTree(nodes[i + 1 :], root, root)

        return self.trees

    def generateTree(self, nodes, root, parent):
        if not len(nodes):
            return

        if len(nodes) == 1:
            if nodes[0] < parent.val:
                parent.left = TreeNode(nodes[0])
            else:
                parent.right = TreeNode(nodes[0])
            self.trees.append(root)
            return
        else:
            for i in range(len(nodes)):
                now = TreeNode(nodes[i])
                if nodes[i] < parent.val:
                    parent.left = now
                else:
                    parent.right = now

                self.generateTree(nodes[:i], root, now)
                self.generateTree(nodes[i + 1 :], root, now)
