#a and b ->a could be answer


#1)So we do bfs traversal and when it some node then we 
#return stuff that is the same as in the question , if its not that then None.

#2)And well recieving both at the same time implies they are under
#Ultimately root will enter the ans cus value and null we take the value.

#SO BASICALLY IF ITS ONE AND NONE TAKE THE NONE BUT IF 2 VALUES TAKE THE PARENT AND MOVE THAT UP.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         if root is None or root == p or root ==q:
                return root
         left=self.lowestCommonAncestor(root.left,p,q)
         right=self.lowestCommonAncestor(root.right,p,q)
            
         if (left==None):
            return right
         elif right==None:
             return left
         else:
            return root
        