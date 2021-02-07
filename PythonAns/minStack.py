class MinStack(object):

    def __init__(self):
        self.q = []

# @param x, an integer
# @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

# @return nothing
    def pop(self):
        self.q.pop()


# @return an integer

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]


# @return an integer

    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]


class MinStack2(object):
    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, x):
        self.stack.append(x)
        self.stackMin.append(x)
        self.stackMin.sort()

    def pop(self):
        for i in range(len(self.stackMin)):
            if self.stackMin[i] == self.stack[-1]:
                self.stackMin = self.stackMin[:i]+self.stackMin[i+1:]
                break

        self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stackMin[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack2()

inp = [-2, 0, -3]
for i in inp:
    obj.push(i)

print(obj.pop())
print(obj.top())
print(obj.getMin())
