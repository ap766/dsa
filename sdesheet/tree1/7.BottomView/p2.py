#Vertical Order Traversal and Find the Last Node.

#1)Obviously we again have a queue storing  node and vertical.And
#A Map Data Struture to store the vertical and node 
#& The other thing is here instead of checking we just overwrite.


#2)Recursive Traversal - Wont work cus  - Check Image copy for that.- Extra logic then(height)
#Time complexity - O(N) and SC - O(N)





from collections import deque
class Solution:
    def bottomView(self, root):
        if root is None:
            return []
        
        mpp = {}
        q = deque([(root, 0)])
        
        while q:
            node, line = q.popleft()
            mpp[line] = node.data #So basically we overwrite.
            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))
        
        ans = []
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])
        
        return ans
    
s=Solution()
    #      10
    #    /    \
    #   20    30
    #  /  \
    # 40   60

