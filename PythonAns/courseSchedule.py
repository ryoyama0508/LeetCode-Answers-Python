from collections import deque
# Definition for a Node.


class Solution(object):
    def canFinish1(self, numCourses, prerequisites):
        forward = {i: set() for i in range(numCourses)}
        backward = dict(set)
        test = dict()
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in forward if len(forward[node]) == 0]
        while stack:
            node = stack.pop()
            # take no connection node
            for neigh in backward[node]:
                # check adjacent node
                # erace direction
                forward[neigh].remove(node)
                # check if there is no direction mark
                if len(forward[neigh]) == 0:
                    # if 0, you can stack
                    stack.append(neigh)
            # erase forward to return not forward at the end of this func
            forward.pop(node)
        return not forward
