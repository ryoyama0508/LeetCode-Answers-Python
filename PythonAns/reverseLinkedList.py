# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        last = head
        now = head.next
        i = 0
        if now.next:
            while now.next:
                nextN = now.next
                now.next = last

                if i == 0:
                    last.next = None

                last = now
                now = nextN
                i += 1

            now.next = last
        else:
            now.next = last
            last.next = None
        return now
