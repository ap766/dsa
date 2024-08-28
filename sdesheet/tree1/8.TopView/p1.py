#We will do level order traversal.

#The same verticals
#The first node is every level will be the top view.

#So again we have a queue to store the node and only the vertical this time.
#And we have a map datastructure for the vertical and node
#So here if the vertical is already in the map then we dont add it.
 

#1)So map stores the top view stuff.
#We needto get it in order.

#2)Also we dont prefer the recursive way as the behind elements might come first , So yes.
from collections import deque
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        if not root:
            return []
        mpp = {}
        q = deque([(root, 0)])
        
        while q:
             node, line = q.popleft()
             if line not in mpp:
                mpp[line] = node.data
             if node.left:
                    q.append((node.left, line - 1))
             if node.right:
                    q.append((node.right,line+1))
              
             ans = []
             for key in sorted(mpp.keys()):
                ans.append(mpp[key])
        
        return ans

    
