#OBSERVE
#Basically like drawing a mirror on the centre.
#Left shows on Right and Vice Versaa

#INTUITION
#The left subtree will have root as root->left
#The right subtree will have root as root->right

#If we do a similar type traversal root is root but left is right and right is left.
#IF WE DO THE TRAVERSAL SIMULTANEOUSLY AND THE NODES ARE SAME WHILE DOING SO.



from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def checksym(self, left, right):
        if left is None and right is None:       
            return True
        elif left is None or right is None:
            return False
        
        return left.val == right.val and self.checksym(left.left, right.right) and self.checksym(left.right, right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checksym(root.left, root.right)
    

