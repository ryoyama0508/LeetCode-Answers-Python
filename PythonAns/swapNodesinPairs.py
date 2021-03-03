class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        prev, curr = head, head.next
        dummy.next = curr

        while curr.next and curr.next.next:
            prev.next, curr.next, prev = curr.next.next, prev, curr.next
            curr = prev.next

        if curr:
            curr.next, prev.next = prev, curr.next

        return dummy.next