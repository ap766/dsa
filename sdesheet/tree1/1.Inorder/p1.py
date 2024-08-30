#Inorder traversal stands as one of the depth-first traversal techniques for navigating nodes in a 
# binary tree. 

# 1)The method starts by exploring the left subtree recursively in the following order: left child, root node, right child.
# 2) Initially, it traverses the left subtree until reaching the leftmost node.
# 3)Upon reaching a null node, signifying the end of a subtree, the recursive process halts.
# 4)Then we visit the current node that had invoked the inorder on its left child. 
# 5)After visiting the current node we visit the right subtree in the inorder manner as well.


# The depth of the recursion stack depends on the height of the tree.
# In the worst case, the tree could be skewed (like a linked list), and the height would be 
# n leading to a recursion stack of depth of n
# In the best case, for a balanced tree, the height would be logn.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.L = []

    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.L.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.L