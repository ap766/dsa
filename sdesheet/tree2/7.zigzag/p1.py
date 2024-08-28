from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        q=deque()
        q.append(root)
        flag=True
        ans=[]
        while q:    
            qlen=len(q)
           
            level=[]
            for i in range(0,qlen):
                
                Node=q.popleft()
               
                if Node:
                   level.append(Node.val)
                   q.append(Node.left)
                   q.append(Node.right)
                
            if level:
                if flag:
                 ans.append(level)
                else:
                 ans.append(level[::-1])
            flag=not flag
            
        return ans