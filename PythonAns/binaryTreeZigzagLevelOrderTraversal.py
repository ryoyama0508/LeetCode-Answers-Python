from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        odd = True
        queue = deque([root])
        ret = [[root.val]]
        self.bfs(queue, ret, odd)
        return ret[:-1]

    def bfs(self, queue, ret, odd):
        if not queue:
            return
        ap = deque([])
        newQ = deque([])
        while queue:
            node = queue.popleft()
            if odd:
                if node.left:
                    newQ.append(node.left)
                    ap.appendleft(node.left.val)
                if node.right:
                    newQ.append(node.right)
                    ap.appendleft(node.right.val)
            else:
                if node.left:
                    newQ.append(node.left)
                    ap.append(node.left.val)
                if node.right:
                    newQ.append(node.right)
                    ap.append(node.right.val)

        ret.append(ap)
        if odd:
            odd = False
        else:
            odd = True
        self.bfs(newQ, ret, odd)
