#1. class Solution:
def __init__(self):
        self.L = []

def postorderTraversal(self,root):
        if root is None:
            return []
       
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.L.append(root.val)

        return self.L
