# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = l3 = ListNode(0)
        while l1 and l2:
            if l3.val + l1.val + l2.val < 10:
                l3.val = l3.val + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
                if l1 or l2:
                    l3.next = ListNode(0)

            else:
                l3.val = l3.val + l1.val + l2.val-10
                l1 = l1.next
                l2 = l2.next
                l3.next = ListNode(1)

            l3 = l3.next

        if l1:
            while l1:
                if l3.val + l1.val < 10:
                    l3.val = l3.val + l1.val
                    l1 = l1.next
                    if l1:
                        l3.next = ListNode(0)

                else:
                    l3.val = l3.val + l1.val-10
                    l1 = l1.next
                    l3.next = ListNode(1)

                l3 = l3.next

        if l2:
            while l2:
                if l3.val + l2.val < 10:
                    l3.val = l3.val + l2.val
                    l2 = l2.next
                    if l2:
                        l3.next = ListNode(0)

                else:
                    l3.val = l3.val + l2.val-10
                    l2 = l2.next
                    l3.next = ListNode(1)

                l3 = l3.next
        return ret
