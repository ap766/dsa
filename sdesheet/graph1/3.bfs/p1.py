from typing import List
from collections import deque
def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
     
    ans=[]
    q=deque()
    q.append(0)
    vis=[0]*n
    vis[0]=1

    while q:
      Node=q.popleft()
      ans.append(Node)
      for neighbour in adj[Node]:
          if not vis[neighbour]:
            q.append(neighbour)
            vis[neighbour]=1
    
    return ans


#Approach - 

#1. We will use a queue to store the nodes of the graph.
#2. We will start by adding the first node to the queue and mark it as visited.
#3. We will pop the first node from the queue and add it to the answer list.
#4. We will iterate over all the neighbours of the node and add them to the queue if they are not visited.
#5. We will mark the neighbour as visited.
#6. We will repeat the above steps until the queue is empty.

#This process continues until the queue becomes empty. Basically till no more neighbours

#Time complexity - O(V+E) where V is the number of vertices and E is the number of edges in the graph.
#Space Complexity - O(3N) - Visited list + queue + bfs(ans

#In the code , a node always goes once into the bfs and runs on all neighbours which is all degrees

#queue of while loop will itself run N times since there are N nodes
#And the for is for total degrees 

#SO O(N)+O(2E) Since 2E is equal to the total degrees since we traverse thru every neighbour also


