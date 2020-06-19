# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        last = head
        now = head.next
        while now != None:
            if now.val == val:
                last.next = now.next
                now = now.next
            else:
                temp = now.next
                last = now
                now = temp

        if head.val == val:
            return head.next

        return head
