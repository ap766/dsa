#1)A node can be a neighbour to 2 nodes without being a cycle so previous techniqye
#2)SO 2 arrays here vis arrys and dfsvisited array - we mark unvisited in the dfsvisistedarray when it goes back  
#That is Basically Cus the Path is Different. On the Same Path Node has to be visited again.
#3)Also well i dont think Parent thing will happen  
#4)Also we can do it in single ARRAY by marking vis as 1 and pathvis as 2

from typing import List

class Solution:
    def dfs(self,node,adj,vis,dfsvis):
        vis[node]=1
        dfsvis[node]=1
        
        for it in adj[node]:
          
            if not vis[it]:
                if self.dfs(it, adj, vis, dfsvis):
                   return True
            elif dfsvis[it]:
                return True
                
        dfsvis[node] = 0
        return False

                


    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        vis=[0 for _ in range(0,V)]
        dfsvis=[0 for _ in range(0,V)]
        for i in range(0,V):
            if not vis[i]:
                if self.dfs(i,adj,vis,dfsvis):
                   return True
               
        return False