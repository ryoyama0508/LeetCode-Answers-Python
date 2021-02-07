class MinStack(object):
    def __init__(self):
        self.val = None
        self.next = None
        self.last = None
        self.min = float("inf")

    def push(self, x):
        self.val = x
        if self.last:
            self.min = min(self.last.min, x)
        else:
            self.min = x

        self.next = MinStack()
        temp = self
        self = self.next
        self.last = temp

    def pop(self):
        self = self.last
        self = MinStack()

    def top(self):
        return self.val

    def getMin(self):
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

inp = [-2, 0, -3]
for i in inp:
    print(obj.val)
    obj.push(i)
    print(obj.last)

obj.pop()
print('top', obj.top())
print('get min', obj.getMin())
