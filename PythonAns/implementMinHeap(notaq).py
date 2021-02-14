class MinHeap:
    def __init__(self, val):
        self.heap = []

    def swap(self, pi, ci, isInsert):
        if isInsert:
            if self.heap[pi] <= self.heap[ci]:
                return
            self.heap[pi], self.heap[ci] = self.heap[ci], self.heap[pi]
            self.swap((pi - 1) / 2, pi, isInsert)
        # getMin
        # if self.heap[i]< self.heap[(2 * i) + 1]:
        #     self.swap((pi - 1) / 2, pi, isInsert)

    def insert(self, val):
        self.heap.append(val)
        l = len(self.heap)
        self.swap((l - 1) / 2, l, True)

    def getMin(self):
        ret = self.heap[0]
        tail = self.heap.pop()
        self.heap.insert(0, tail)
        # self.swap(
        #     0,
        # )


# coundnt implement try later