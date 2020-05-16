# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        list1 = []
        list1.append(head.val)
        while head.next:
            list1.append(head.next.val)
            head = head.next

        list2 = []
        i = len(list1)-1
        while i > -1:
            list2.append(list1[i])
            i -= 1

        j = 0
        while j < len(list2)-1:
            if list1[j] != list2[j]:
                return False
            j += 1

        return True


class falseSolution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        sum = 0
        isTrue = self.xor(head, sum)
        return isTrue

    def xor(self, head, sum):
        print(sum, "before")
        sum ^= head.val
        print(sum, "after")

        if head.next:
            return self.xor(head.next, sum)
        else:
            if sum == 0:
                return True
            else:
                return False
