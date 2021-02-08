# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        dicAdd = {}

        while headA:
            dicAdd[id(headA)] = 0
            headA = headA.next

        while headB:
            if id(headB) in dicAdd:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode2(self, headA, headB):
        lastA, lastB = headA, headB
        countA, countB = 0, 0
        nowA, nowB = headA, headB
        while nowA:
            if nowA.next is None:
                lastA = nowA
            nowA = nowA.next
            countA += 1

        while nowB:
            if nowB.next is None:
                lastB = nowB
            nowB = nowB.next
            countB += 1

        if countA == countB:
            retA, retB = headA, headB
            while retA != retB:
                if retA.next is None or retB.next is None:
                    return None
                retA = retA.next
                retB = retB.next
            return retA
        elif countA > countB:
            if lastA == lastB:
                tmp = headA
                for _ in range(countA - countB):
                    tmp = tmp.next

                retA, retB = tmp, headB
                while retA != retB:
                    retA = retA.next
                    retB = retB.next
                return retA
            return None
        else:
            if lastA == lastB:
                tmp = headB
                for _ in range(countB - countA):
                    tmp = tmp.next
                retA, retB = headA, tmp
                while retA != retB:
                    retA = retA.next
                    retB = retB.next
                return retA
            return None
