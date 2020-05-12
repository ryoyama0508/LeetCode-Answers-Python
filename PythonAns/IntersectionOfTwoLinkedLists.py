# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):  # TLE
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        list = []
        list.append(hex(id(headA)))

        while headA.next:
            list.append(hex(id(headA.next)))
            headA = headA.next

        if hex(id(headB)) in list:
            return headB

        while headB.next:
            if hex(id(headB.next)) in list:
                return headB.next
            headB = headB.next

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        hash = {}

        hash[headA.val] = hex(id(headA))

        while headA.next:
            exist = hash.get(headA.next.val)
            if exist:
                hash[str(headA.next.val) + "v2"] = hex(id(headA.next))
            else:
                hash[headA.next.val] = hex(id(headA.next))
            headA = headA.next

        value = hash.get(headB.val)
        if value:
            if hash[headB.val] == hex(id(headB)):
                return headB

        while headB.next:
            value = hash.get(headB.next.val)

            if value:
                if value == hex(id(headB.next)) or str(value) + "v2" == hex(id(headA.next)):
                    return headB.next

            headB = headB.next
