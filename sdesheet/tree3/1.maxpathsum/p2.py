#Valofnode +(maxl+maxr) - check in image
#So we find this curve for every node - and the max should be the answer

#So just like diameter here calculate the node and left + right's sum
#extra is take zero if its coming as negative.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxpathsum=float('-inf')
    
    def height(self,root):
        if root is None:
            return 0
        
        l=max(0,self.height(root.left)) #It could end up being a negative value in that case its better to not take.
        r=max(0,self.height(root.right))
        
        self.maxpathsum=max(self.maxpathsum,l+r+root.val)
        
        return root.val+max(l,r)
        
        
    def maxPathSum(self,root) -> int:
        self.height(root)  # Initiate the height function to compute max path sum
        return self.maxpathsum
        