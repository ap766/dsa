from typing import List
from collections import deque


class Solution:
    def bfs(self,node,color,graph,q):
           
        q.append(node)
        color[node] = 0           
        while q:
                    node = q.popleft()
                    for neighbour in graph[node]:
                        if color[neighbour] == -1:
                            color[neighbour] = 1 - color[node]
                            q.append(neighbour)
                        elif color[neighbour] == color[node]:
                            return False
                        
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V
        q=deque()
        
        for node in range(V):
            if color[node] == -1:
                if not self.bfs(node,color,graph,q):
                    return False
                
        return True