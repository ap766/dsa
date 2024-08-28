#1)Going depth wise - so recursion
#2)vis array
#3)neighbour in adj list and run for each loop and go to the depth when call over next dfs


# Time Complexity: For an undirected graph, O(N) + O(2E), For a directed graph, O(N) + O(E), Because for every node we are calling the recursive function once, the time taken is O(N) and 2E is for total degrees as we traverse for all adjacent nodes.

# Space Complexity: O(3N) ~ O(N), Space for dfs stack space, visited array and an adjacency list.

#User function Template for python3

class Solution:
    
    def dfs(self,node,vis,adj,ls):
        vis[node]=1
        ls.append(node)
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it,vis,adj,ls)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        
        
        vis=[0]*V
        start=0
        ls=[]
        self.dfs(start,vis,adj,ls)
        return ls
       
