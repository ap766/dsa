class Solution:
    def bfs(self,image,sr,sc,color):
        q=collections.deque()
        q.append([sr,sc])
        
        originalcolor=image[sr][sc]
        image[sr][sc]=color
        
        while q:
            i,j=q.popleft()
            for pos in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                r,c=pos[0],pos[1]
                if r<len(image) and r>=0 and c<len(image[0]) and c>=0 and image[r][c]==originalcolor and image[r][c]!=color:
                    q.append([r,c])
                    image[r][c]=color
                   
        
        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.bfs(image,sr,sc,color)
        return image