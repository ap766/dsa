
#Honestly method makes no sense bcus we are repeating the stuff whoch we willanyways traverse
#basically the lower nodes for no reason



from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxdiam = 0
    
    def height(self, root):
        if not root:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        return 1 + max(l, r)
        
    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node):
            if not node:
                return 0
            
            l = self.height(node.left)
            r = self.height(node.right)
            
            self.maxdiam = max(self.maxdiam, l + r)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.maxdiam