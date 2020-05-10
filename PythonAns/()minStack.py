class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        :type val: int
        :type next: self
        """
        self.val = None
        self.next = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.val is None:
            self.val = x
            return

        newNode = self

        if newNode.next:
            while newNode.next:
                newNode = newNode.next

            newNode.next = MinStack()
            newNode.next.val = x

        else:
            newNode.next = MinStack()
            newNode.next.val = x

        return

    def pop(self):
        """
        :rtype: None
        """
        oldNode = self
        newNode = self
        while newNode.next:
            oldNode = newNode
            newNode = newNode.next

        oldNode.next = None
        return

    def top(self):
        """
        :rtype: int
        """
        newNode = self
        while newNode.next:
            newNode = newNode.next

        return newNode.val

    def getMin(self):
        """
        :rtype: int
        """
        if self.val is None:
            return None

        newNode = self
        min = newNode.val
        while newNode.next:
            if newNode.next.val < min:
                min = newNode.next.val
            newNode = newNode.next

        if newNode.val < min:
            min = newNode.val
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
