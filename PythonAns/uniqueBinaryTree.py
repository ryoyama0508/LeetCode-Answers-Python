class Solution(object):
    def numTrees(self, n):
        G = [1, 1, 2]+[0]*(n-2)
        for i in range(3, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]

        return G[n]
