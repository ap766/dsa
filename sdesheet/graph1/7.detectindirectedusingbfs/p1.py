#okay so topo final wont be equal to v - sAME kAHN'S

from typing import List
from collections import deque

class Solution:
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        indegree = [0] * V
        topo = []
        
        for i in range(V):
            for neighbour in adj[i]:
                indegree[neighbour] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)
           
        return len(topo) != V