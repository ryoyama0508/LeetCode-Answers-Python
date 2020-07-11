class Solution(object):
    def isValidBST(self, root):
        if root is None or (not root.left and not root.right):
            return True
        tmp = root
        while tmp.left:
            tmp = tmp.left
        stack, big = [], tmp.val-1
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if node.val <= big:
                return False
            big = node.val
            root = node.right
        return True
