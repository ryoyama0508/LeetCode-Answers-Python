class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        res = []
        cnt = 0
        for x in sorted(intervals, key=lambda x: x[1]):
            if res and x[0] < res[-1][1]:
                print(x[0], res[-1][1])
                cnt += 1
            else:
                res.append(x)
            print(res)
        return cnt

    def eraseOverlapIntervals2(self, intervals):
        end, cnt = float('-inf'), 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end:
                end = i[1]
            else:
                cnt += 1
        return cnt
