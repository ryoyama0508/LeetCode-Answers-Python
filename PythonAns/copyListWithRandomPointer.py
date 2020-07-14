
# Definition for a Node.


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        seen = {}

        def dfs(head):
            if head in seen:
                return seen[head]
            if not head:
                return None
            cp = Node(head.val)
            seen[head] = cp
            cp.next = dfs(head.next)
            cp.random = dfs(head.random)
            return cp
        return dfs(head)
