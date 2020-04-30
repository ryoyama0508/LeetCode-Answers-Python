# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # couldnt solve because how to set the first value
        newList = l1

        if l1.next is None and l2.next is None:
            if l1.val > l2.val:
                newList.val, newList.next = l2.val, l1
                return newList

        n1 = l1
        n2 = l2
        if l1.val <= l2.val:
            n2 = l2.next
            newList = l2
        else:
            n1 = l1.next

        n = newList

        while n1 and n2:
            if n1.val <= n2.val:
                n.next = n1
                n1 = n1.next
            else:
                n.next = n2
                n2 = n2.next

            n = n.next

        if n1 is None:
            n.next = n2
        elif n2 is None:
            n.next = n1

        return newList
