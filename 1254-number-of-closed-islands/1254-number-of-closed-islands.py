class Solution:
    def dfs(self,grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=0:
            return
        grid[r][c] = 1 
        self.dfs(grid, r + 1, c)
        self.dfs(grid,r - 1, c)
        self.dfs(grid,r, c + 1)
        self.dfs(grid,r, c - 1)
    def closedIsland(self, grid: list[list[int]]) -> int:
        count = 0 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or r == len(grid)-1 or c == 0 or c == len(grid[0])-1:
                    self.dfs(grid,r,c)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    self.dfs(grid,r,c)
                    count+=1 
        return count