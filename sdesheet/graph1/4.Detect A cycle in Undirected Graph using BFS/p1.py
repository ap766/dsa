#1)The cycle in a graph starts from a node and ends at the same node. So we can think of two algorithms to do this, in this article we will be reading about the BFS, and in the next, we will be learning how to use DFS to check. 
#Started in different paths and collide.

#2)So yes, since bfs we start in a queue, but we also need to store the parent here , for the first one parent -1 bcus next pt

#3)Now they are saying it will be filled in the visited array but what abt repeating neighbours how we diff? Ig someone at the same level has to .
#So it is like if someone is visited and it did not come from the parent. 


#4)ALso there could be case of multiple components.

from typing import List
import collections

class Solution:
    
    def bfs(self, node, adj, vis):
        q = collections.deque()
        q.append((node, -1))
        vis[node] = 1
        
        while q:
            node, parent = q.popleft()
            for neighbour in adj[node]:
                if vis[neighbour]:
                    if parent != neighbour:
                        return True
                else:
                    vis[neighbour] = 1
                    q.append((neighbour, node))
        return False
                
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.bfs(i, adj, vis):
                    return True
        return False