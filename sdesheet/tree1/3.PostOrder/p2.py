class Solution:
    def postorderTraversal(self, root):
        
        st1=[]
        st2=[]
        st1.append(root)
        
        while st1:
            node=st1.pop()
            if node:
                st2.append(node.val)
                st1.append(node.left)
                st1.append(node.right)
        return st2[::-1]
