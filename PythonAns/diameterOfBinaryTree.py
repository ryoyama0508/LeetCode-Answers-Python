# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diam = []
        _, diam = self.depth(root, diam)

        print(diam)
        biggest = 0
        for d in diam:
            if d > biggest:
                biggest = d

        return biggest

    def depth(self, root, diam):
        if root is None:
            return 0, diam
        rightDep = self.depth(root.right, diam)
        leftDep = self.depth(root.left, diam)
        ret = 0
        if rightDep <= leftDep:
            ret = leftDep + 1
        else:
            ret = rightDep + 1

        if rightDep == 0 and leftDep == 0:
            diam.append(2)
        elif rightDep == 0 and leftDep != 0:
            diam.append(leftDep + 1)
        elif rightDep != 0 and leftDep == 0:
            diam.append(rightDep + 1)
        return ret, diam
