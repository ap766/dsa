#Mainly Indegree thing , ones with zero indree of cure they will be in the start because nothing comes before it 
#And basically now as these visit the neighbour , the indgree oculd become zero eenually means nothing else beore them



#STEPS
#Insert all nodes with Nidregree Zeo


from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree=deque()
        indegree=[0]*V
        topo=[]
        
        for i in range(0,V):
            for neighbour in adj[i]:
                indegree[neighbour]+=1
        
        q=deque()
        for i in range(0,V):
            if indegree[i]==0:
               q.append(i)
        
        while q:
            node=q.pop()
            topo.append(node)
            for it in adj[node]:
                indegree[it]-=1
                
                if (indegree[it]==0):
                    q.append(it)
                    
        return topo
        