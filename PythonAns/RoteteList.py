class Solution:
    def rotateRight(self, head, k):
        if k == 0 or head is None:
            return head

        countNode = head
        c = 0
        while countNode:
            countNode = countNode.next
            c += 1

        if k >= c:
            k = k % c

        if k == 0:
            return head

        i = 0
        late = fast = head
        while i < k:
            fast = fast.next
            i += 1

        while fast.next:
            fast = fast.next
            late = late.next

        ret = late.next
        late.next = None
        fast.next = head
        return ret
