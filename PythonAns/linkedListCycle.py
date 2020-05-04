# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        addressDic = {}
        isTrue = self.chaseCircle(head, addressDic)
        return isTrue

    def chaseCircle(self, head, addressDic):
        if head is None:
            return False

        addressDic[head.val] = head.next
        if head.val in addressDic:
            if addressDic[head.val] == head.next:
                return True
        self.chaseCircle(head.next, addressDic)
