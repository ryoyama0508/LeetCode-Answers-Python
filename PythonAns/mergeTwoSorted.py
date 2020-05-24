# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

        n1 = l1
        n2 = l2

        ret = currNode = ListNode(0)

        if n1.val <= n2.val:
            currNode = n1
            ret = currNode
            if n1.next:
                n1 = n1.next
            else:
                n1.next = n2
                return ret
        else:
            currNode = n2
            ret = currNode
            if n2.next:
                n2 = n2.next
            else:
                n2.next = n1
                return ret

        while True:
            if n1.val <= n2.val:
                currNode.next = n1
                currNode = currNode.next

                if n1.next:
                    n1 = n1.next
                else:
                    break
            else:
                currNode.next = n2
                currNode = currNode.next

                if n2.next:
                    n2 = n2.next
                else:
                    break

        if n1.next is None:
            currNode.next = n2
        elif n2.next is None:
            currNode.next = n1
        else:
            if currNode.val == n1.val:
                currNode.next = n2
            elif currNode.val == n2.val:
                currNode.next = n1

        return ret
