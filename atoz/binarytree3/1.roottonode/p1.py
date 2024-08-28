

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getPath(self,root,arr,x):
        if not root:
            return False
        
        #1.
        arr.append(root.val)

        #2.
        if root.val == x:
            return True
        
        if self.getPath(root.left,arr,x) or self.getPath(root.right,arr,x):
            return True 
        #3.
        arr.pop()
        return False
    
    def solve(self,A,B):
        arr=[]
        if not A:
            return arr
        
        self.getPath(A,arr,B)
        return arr
    
