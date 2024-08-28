# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getheight(self,root):
        if root is None:
            return 0
        
        l=self.getheight(root.left)
        r=self.getheight(root.right)
        
        return max(l, r) + 1
        
        
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        
        
        l=self.getheight(root.left)
        r=self.getheight(root.right)
        
        if (abs(l-r)<=1) and self.isBalanced(root.left) and self.isBalanced(root.right): 
           return True
        
        return False