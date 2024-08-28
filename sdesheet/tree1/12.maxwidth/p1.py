#INTUITION

#If the nodes were indexed it would be so simple just subtract.
#1)But this fails (the pic stuff) , 2*() will be overflow for skew trees
#So instead at each level maybe we could have have it as 1 to n how?


#1)So if there is i , make i - min on the level , and then calxulate 2i+1 2i+2 
#2And then take the left most and right most and the ans we get

#APPROACH - maybe use a queue  and width.

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        ans=0
        if not root:
            return 0
        q=deque([(root,0)])
        while q :
            size=len(q)
            mmin=q[0][1] #S1)a) To get the minimum
            first,last=None,None
            for i in range(size):
                #S1)b)To calculate based on that for the following
                cur_id=q[i][1]-mmin
          
                node = q[i][0]
                if node.left:
                    q.append((node.left,cur_id*2+1))
                if node.right:
                    q.append((node.right,cur_id*2+2))
                   
                #2)Assigning them.For finding the answer.
                if i==0:
                    first=cur_id
                if i==size-1:
                    last=cur_id
                    
            ans=max(ans,last-first+1)
            print(ans)
                        
            # Remove the processed nodes of the current level
            for _ in range(size):
                q.popleft()
        
        return ans
                