from collections import deque
class Solution:
    def bfs(self,i,j,grid,vis):
        q=collections.deque()
        vis[i][j]=1
        q.append([i,j])
        while q:
            i,j=q.popleft()
            for pos in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
                r,c=pos[0],pos[1]
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and not vis[r][c] and grid[r][c]=="1":
                    q.append([r,c])
                    vis[r][c]=1
            
            
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        ct=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if not vis[i][j] and grid[i][j]=="1":
                    self.bfs(i,j,grid,vis)
                    ct+=1
        return ct