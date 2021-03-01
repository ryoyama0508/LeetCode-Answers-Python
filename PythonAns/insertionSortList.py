# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        if head is None:
            return None

        curr = head.next
        while curr:
            if curr.val < head.val:
                head, curr.next, curr = curr, head, curr.next
                continue

            tmp, tmp_next = head, head.next
            while tmp_next != curr:
                print(tmp.val, tmp_next.val, curr.val)
                if curr.val < tmp_next.val:
                    tmp.next, curr.next, tmp_next.next, curr = (
                        curr,
                        tmp_next,
                        curr.next,
                        curr.next,
                    )
                    print(curr.val, head)
                    break

                tmp, tmp_next = tmp_next, tmp_next.next
            if curr is None:
                break
            if tmp_next == curr:
                curr = curr.next

        return head