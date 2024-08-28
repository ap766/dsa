# Preorder traversal is one of the depth-first traversal methods used to explore nodes in a binary tree. The algorithm first visits the root node then in the preorder traversal, we visit (ie. add to the array) the current node by accessing its value then we recursively traverse the left subtree in the same manner. We repeat these steps for the left subtree then when we return to the current node, we recursively travel to the right subtree in a preorder manner as well.The sequence of steps in preorder traversal follows: Root, Left, Right.

class Solution:
    def __init__(self):
        self.L = []

    def preorderTraversal(self,root):
        if root is None:
            return []
        self.L.append(root.val)
        self.preorderTraversal(root.left)
       
        self.preorderTraversal(root.right)

        return self.L
