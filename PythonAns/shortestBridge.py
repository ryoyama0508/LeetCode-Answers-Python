class Solution(object):
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = "#"
            bfs.append((i, j))
            for x, y in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 1:
                    dfs(x, y)

        def find():
            first = False
            for i in range(0, len(A)):
                for j in range(0, len(A[0])):
                    if A[i][j] == 1:
                        dfs(i, j)
                        first = True
                        break
                if first == True:
                    break
        bfs = []
        step = 0
        find()

        while bfs:
            new = []
            for i, j in bfs:
                for x, y in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
                    if 0 <= x < len(A) and 0 <= y < len(A[0]):
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = "#"
                            new.append((x, y))
            step += 1
            bfs = new
