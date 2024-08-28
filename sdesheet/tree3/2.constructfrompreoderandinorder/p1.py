#Inorder in hashmap
#2 pointers - prestart and preend and instart and inend.

#So first preorder. At the prestart
#And based on that we get the inroot
#Now using the difference (numsleft) which was istart-iroot and the prestart to get the new preoder and also similarly get the inorder -1 and the other preoder by dong + and also the inorder by doing +

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        inMap = {val: idx for idx, val in enumerate(inorder)}
        root = self._buildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        return root
    def _buildTree(self,preorder,preStart,preEnd,inorder,inStart,inEnd,inMap):
        if preStart>preEnd or inStart>inEnd:
            return None
        #1)
        root=TreeNode(preorder[preStart])
        inRoot=inMap[root.val]
        
        #2)
        numsLeft=inRoot-inStart
        root.left=self._buildTree(preorder,preStart+1,preStart+numsLeft,inorder,inStart,inRoot-1,inMap)
        root.right = self._buildTree(preorder, preStart + numsLeft + 1, preEnd,inorder, inRoot + 1, inEnd, inMap)
        
        return root