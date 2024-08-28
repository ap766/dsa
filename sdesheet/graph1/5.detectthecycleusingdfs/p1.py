from typing import List
import collections

class Solution:
    
    def traversal(self, node, adj, vis,parent):
      
        vis[node] = 1
        
        for neighbour in adj[node]:
                if vis[neighbour]:
                    if parent != neighbour:
                        return True
                else:
                    if self.traversal(neighbour,adj,vis,node):
                        return True
                    
        return False
                
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.traversal(i, adj, vis,-1):
                    return True
        return False

#So here in inutuition is actually kinda sames but here one dfs is enough to make a full cycle and here we dont have queue so we send the parent node in the recursiove call
