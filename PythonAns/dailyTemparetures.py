from collections import deque


class Solution(object):
    def dailyTemperatures(self, T):
        ret = deque()
        recentNumHash, m, numList = {}, 0, deque()
        for i in range(len(T)-1, -1, -1):
            if m <= T[i]:
                ret.appendleft(0)
                m = T[i]
                recentNumHash = {T[i]: i}
                numList = deque()
                numList.appendleft(T[i])
            else:
                for num in numList:
                    if num > T[i]:
                        ret.appendleft(recentNumHash[num] - i)
                        break
                if numList[0] != T[i]:
                    numList.appendleft(T[i])
                recentNumHash[T[i]] = i

        return ret
