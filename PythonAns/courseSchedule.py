class Solution:
    def canFinish(self, n, pres):
        from collections import deque
        outdegree = [[] for _ in range(n)]
        indegree = [0] * n

        for p in pres:
            indegree[p[0]] += 1
            outdegree[p[1]].append(p[0])

        dq = deque()
        for i in range(n):
            if indegree[i] == 0:
                dq.append(i)

        result = []
        while dq:
            x = dq.popleft()
            result += [x]
            for i in outdegree[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    dq.append(i)
        return len(result) == n


obj = Solution()
print(obj.canFinish(3, [[1, 0], [2, 1]]))
