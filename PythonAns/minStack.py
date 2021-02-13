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
                self.stackMin = self.stackMin[:i] + self.stackMin[i + 1 :]
                break

        self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stackMin[0]


class Node(object):
    def __init__(self, val):  # might delete
        self.val = val
        self.next = None
        self.min = float("inf")


class MinStack3(object):
    def __init__(self):
        self.head = None  # leave none at the bottom of stack

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def push(self, val):
        if self.isEmpty():
            min_sofar = float("inf")
        else:
            min_sofar = self.head.min

        new_node = Node(val)  # create obj
        new_node.next = self.head
        self.head = new_node  # reset head
        self.head.min = min(min_sofar, self.head.val)

    def pop(self):
        if self.isEmpty():
            return None

        poped_node = self.head
        self.head = self.head.next
        poped_node.next = None  # delete poped node
        return poped_node.val

    def top(self):
        if self.isEmpty():
            return None

        return self.head.val

    def getMin(self):
        if self.isEmpty():
            return None

        return self.head.min

    def display(self):

        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")

        else:

            while iternode != None:

                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return


# Your MinStack object will be instantiated and called as such:
obj = MinStack3()

inp = [-2, 0, -3]
for i in inp:
    obj.push(i)

print(obj.pop())
print(obj.top())
print(obj.getMin())
