class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy = dist = ListNode(0)
        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                while prev.val == curr.val:
                    curr = curr.next
                    if curr is None:
                        dist.next = curr
                        return dummy.next
                prev = curr
                curr = curr.next

            else:
                dist.next = prev
                dist = dist.next
                prev = curr
                curr = curr.next

        dist.next = prev
        return dummy.next