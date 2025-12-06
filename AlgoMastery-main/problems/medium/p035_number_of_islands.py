"""
Task 35: Number of Islands

Given a 2D grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Example:
    number_of_islands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) -> 3

    number_of_islands([
        ["1","0","1","1","0","1","1"]
    ]) -> 3
"""

from typing import Any, List

def isvalid(self,i,j,n,m,grid):
        if (i>=0 and i<n) and (j>=0 and j<m) and grid[i][j]=='1' :
            return True
        return False

def dfs(self,i,j,n,m,vis,grid):
        vis[i][j]=1
        if self.isvalid(i+1,j,n,m,grid) and vis[i+1][j]==0:
            self.dfs(i+1,j,n,m,vis,grid)
        if self.isvalid(i-1,j,n,m,grid) and vis[i-1][j]==0:
            self.dfs(i-1,j,n,m,vis,grid)
        if self.isvalid(i,j-1,n,m,grid) and vis[i][j-1]==0:
            self.dfs(i,j-1,n,m,vis,grid)
        if self.isvalid(i,j+1,n,m,grid) and vis[i][j+1]==0:
            self.dfs(i,j+1,n,m,vis,grid)
        

def numIslands(self, grid: List[List[str]]) -> int:

        count=0
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for _ in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and vis[i][j]==0:
                    count+=1
                    self.dfs(i,j,n,m,vis,grid)
        return count