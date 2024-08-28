#So whenever dfs is complete we store that in the stack, cus that portion is visited so everything would be there and linear ordering would be followed
class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    def dfs(self,node,vis,adj,st):
        
        vis[node]=1
        for neighbour in adj[node]:
            if not vis[neighbour]:
                self.dfs(neighbour,vis,adj,st)
        st.append(node) #okay reason we put it here is bcus that means that ones dfs is done if inside it will be appended before done 
        
        
        
    def topoSort(self, V, adj):
        
        st=[]
        vis=[0]*V
        for i in range(0,V):
            if not vis[i]:
               self.dfs(i,vis,adj,st)
        
        ans=[]
        while st:
            ans.append(st.pop())
        
        return ans
        
            
