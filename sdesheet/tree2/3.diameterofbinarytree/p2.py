# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxdiameter = 0
    
    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.maxdiameter = max(self.maxdiameter, l + r)
            
            return 1 + max(l, r)
        
        dfs(root)
        return self.maxdiameter