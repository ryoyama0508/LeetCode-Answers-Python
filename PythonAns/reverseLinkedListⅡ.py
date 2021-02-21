class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            print(right.values)
            print(m, "m")
            print(n, "n")
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

    def reverseBetween2(self, head, m, n):
        if head is None:
            return None

        prev, curr = None, head
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1

        connectiong1 = prev
        connectiong2 = curr
        while n > 1:
            prev, prev.next, curr = curr, prev, curr.next
            n -= 1

        if connectiong1:
            connectiong1.next = prev
        else:
            head = prev
        connectiong2.next = curr

        return head

    def reverseBetween3(self, head, m, n):
        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

    def reverseBetween4(self, head, m, n):
        if head is None:
            return head

        connecting = tmp = head
        c = 1
        while c < m:
            connecting = tmp
            tmp = tmp.next
            c += 1

        rev = None
        now = tmp
        while c < n + 1:
            rev, rev.next, now = now, rev, now.next
            c += 1
        print(head)
        connecting.next = rev
        tmp.next = now

        return head
