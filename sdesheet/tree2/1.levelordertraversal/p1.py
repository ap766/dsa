#Intuition -> 
from collections import deque
class Solution:
    def levelOrder(self, root):
        q=deque()
        q.append(root)
        res=[]
        
        while q:
            level=[]
            for i in range(0,len(q)):
                Node=q.popleft()
                if Node:
                    level.append(Node.val)
                    q.append(Node.left)
                    q.append(Node.right)
            if level: 
                res.append(level)
        return res
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.
    