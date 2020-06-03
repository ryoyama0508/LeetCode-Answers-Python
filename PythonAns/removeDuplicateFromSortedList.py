# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print(head)
        if head is None:
            return None

        if head.next:
            return head

        i = head
        j = head.next
        print(head.next.val)

        while j.next:
            if i.val != j.val:
                i.next = j
                i = j
                j = j.next
            else:
                j = j.next
