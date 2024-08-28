from typing import List

class Solution:
    def dfs(self, node, color, graph):
        for neighbour in graph[node]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[node]
                if not self.dfs(neighbour, color, graph):
                    return False
            elif color[neighbour] == color[node]:
                return False
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V
        
        for node in range(V):
            if color[node] == -1:
                color[node] = 0
                if not self.dfs(node, color, graph):
                    return False
                
        return True