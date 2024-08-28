#O(N2) in GFG
#WE will lern O(N)

#INUITION
#While going down increase the value of the children to that of the root node(maxx possible) ubless the sum is larger


#THE VIDEO QUESTION                          
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def changeTree(self, root):
        # Base case: If the current node
        # is None, return and do nothing.
        if root is None:
            return

        # 1)Calculate the sum of the values of
        # the left and right children, if they exist.
        child = 0
        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val

        # 2)Compare the sum of children with
        # the current node's value and update
        if child >= root.val:
            root.val = child
        else:
            # If the sum is smaller, update the
            # child with the current node's value.
            if root.left:
                root.left.val = root.val
            elif root.right:
                root.right.val = root.val

        # Recursively call the function
        # on the left and right children.
        self.changeTree(root.left)
        self.changeTree(root.right)

        # 3)Calculate the total sum of the
        # values of the left and right
        # children, if they exist.
        tot = 0
        if root.left:
            tot += root.left.val
        if root.right:
            tot += root.right.val

        # If either left or right child
        # exists, update the current node's
        # value with the total sum.
        if root.left or root.right:
            root.val = tot


# Function to print the inorder
# traversal of the tree
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)


# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()

# Print the inorder traversal
# of tree before modification
print("Binary Tree before modification:", end=" ")
inorderTraversal(root)
print()

# Call the changeTree function
# to modify the binary tree
sol.changeTree(root)

# Print the inorder traversal
# after modification
print("Binary Tree after Children Sum Property:", end=" ")
inorderTraversal(root)
print()
                           
                        

#FOR THE GFG QUESTION

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
  
        
    def isSumProperty(self, root):
        if root is None:
            return 1
        
        child_sum = 0
        if root.left:
            child_sum += root.left.data
        if root.right:
            child_sum += root.right.data
        
        if (root.left or root.right) and root.data != child_sum:
            return 0
        
        left_check = self.isSumProperty(root.left)
        right_check = self.isSumProperty(root.right)
        
        return left_check and right_check



