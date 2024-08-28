

from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    pre, in_order, pos = [], [], []
    if root is None:
        return [pre, in_order, pos]
    
    stack = [(root, 1)]
    while stack:
        node, state = stack.pop()  # Popping is better instead of making the change while in the stack.
        if state == 1:
            pre.append(node.data)
            stack.append((node, state + 1))
            if node.left:
                stack.append((node.left, 1))
        elif state == 2:
            in_order.append(node.data)
            stack.append((node, state + 1))
            if node.right:
                stack.append((node.right, 1))
        elif state == 3:
            pos.append(node.data)
    
    return [pre, in_order, pos]

# Example usage:
# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# root.left.left = BinaryTreeNode(4)
# root.left.right = BinaryTreeNode(5)
# print(getTreeTraversal(root))  # Output: [[1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1]]