class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack, ret = [root], []
        while stack:
            if root.left is None and root.right is None:
                tmp = stack.pop()
                ret.append(tmp.val)
                if stack:
                    root = stack[-1]
                continue
            if root.left:
                stack.append(root.left)
                tmp = root
                root = root.left
                tmp.left = None
            else:
                tmp = stack.pop()
                ret.append(tmp.val)
                stack.append(root.right)
                root = root.right

        return ret

        # iteratively


def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
