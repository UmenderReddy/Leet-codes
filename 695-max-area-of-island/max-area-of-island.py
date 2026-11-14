class Solution:
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
            return 0
        grid[i][j]=0
        area=1

        area+=self.dfs(grid,i+1,j)
        area+=self.dfs(grid,i-1,j)
        area+=self.dfs(grid,i,j+1)
        area+=self.dfs(grid,i,j-1)
        return area
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=self.dfs(grid,i,j)
                    max_area=max(max_area,area)
        return max_area
        