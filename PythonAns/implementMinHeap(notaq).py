import heapq

# in order to implement of heap by myself, read heapq
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

    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.heap.append(item)
        self._siftdown()

    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()  # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup()
            return returnitem
        return lastelt

    # 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
    # is the index of a leaf with a possibly out-of-order value.  Restore the
    # heap invariant.
    def _siftdown(self):
        new_node_pos = len(self.heap) - 1
        new_node = self.heap[new_node_pos]
        while new_node_pos > 0:
            parent_pos = new_node_pos - 1 // 2
            parent = self.heap[parent_pos]
            if parent > new_node:
                self.heap[new_node_pos] = parent
                new_node_pos = parent_pos
                continue
            else:
                break
        self.heap[new_node_pos] = new_node

    def _siftup(self):
        endpos = len(self.heap)
        newitem_pos = 0
        newitem = self.heap[newitem_pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 1  # leftmost child position from the root
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[newitem_pos] = self.heap[childpos]
            newitem_pos = childpos
            childpos = 2 * newitem_pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[newitem_pos] = newitem
        # _siftdown(heap, startpos, newitem_pos)

        # ここやり直し

    def getMin(self):
        ret = self.heap[0]
        tail = self.heap.pop()
        self.heap.insert(0, tail)
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, 4)


# coundnt implement try later