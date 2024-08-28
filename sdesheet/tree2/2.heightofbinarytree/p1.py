# Definition for a binary tree node.

#I'd say here we are considering max height in a recursive way so max height considering the calling node to be the root node.
#OR U CAN SAY HEIGHT OF SUBTREES 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        print("root",root)
        if root is None:
            return 0
    

        l=self.maxDepth(root.left)

        r=self.maxDepth(root.right)
        
        print("l",l)
        print("r",r)
        return 1+max(l,r)
    
s=Solution()
#[3,9,20,null,null,15,7]
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
#Draw
#     3
#    / \
#   9  20
#     /  \
#    15   7

print(s.maxDepth(root)) #3