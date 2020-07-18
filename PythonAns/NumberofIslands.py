class Solution(object):
    def numIslands(self, grid):
        if grid == []:
            return 0
        c = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    c += 1
        return c

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] != '1':
            return
        grid[i][j] = "#"
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
