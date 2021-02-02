from heapq import heappush, heappop
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        curr_time, h = 0, []
        for k, v in Counter(tasks).items():
            heappush(h, (-1*v, k))

        print(h)
        '''
        heap is in small to big order
        '''
        while h:
            print(h, 'result heap')
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x, y = heappop(h)
                    if x != -1:
                        temp.append((x+1, y))
                if not h and not temp:
                    break
                else:
                    i += 1
                print(h, 'heap while loop')

            for item in temp:
                heappush(h, item)
        return curr_time


obj = Solution()
print(obj.leastInterval(["A", "A", "A", "B", "B", "B", "C"], 2))
