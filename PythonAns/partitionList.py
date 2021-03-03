class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None

        greater_dummy = ListNode(0)
        greater = greater_dummy

        smaller_dummy = ListNode(0)
        smaller = smaller_dummy

        curr = head
        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next