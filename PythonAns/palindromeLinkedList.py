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
        i = len(list1) - 1
        while i > -1:
            list2.append(list1[i])
            i -= 1

        j = 0
        while j < len(list2) - 1:
            if list1[j] != list2[j]:
                return False
            j += 1

        return True

    def isPalindrome2(self, num: int) -> bool:
        str_num = str(num)
        len_num = len(str_num)
        if len_num == 1:
            return True
        if num < 0:
            return False

        rev_str_num = str_num[len_num::-1]
        if len(rev_str_num) != len_num or int(rev_str_num) != num:
            return False
        else:
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

    def isPalindrome3(self, head):
        if head is None:
            return True
        elif head.next is None:
            return True
        elif head.next.next is None:
            if head.val == head.next.val:
                return True
            else:
                return False
        c = -1
        now = head
        while now:
            now = now.next
            c += 1

        odd = False
        if c % 2 == 0:
            odd = True
        print(odd)

        mid_c = c // 2 - 1
        right, left, late, = (
            head.next.next,
            head.next,
            head,
        )
        head.next = None
        print(mid_c)
        if mid_c == 0:
            left.next = late
        else:
            for _ in range(mid_c):
                left.next = late
                late = left
                left = right
                right = right.next

        print(left.val, right.val)

        if odd is True:
            left = left.next

        print(left.val, right.val)

        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next

        return True


obj = Solution()
print(obj.isPalindrome2(1))

# test