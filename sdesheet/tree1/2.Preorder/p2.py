#First Right then left in STack
#Because first left then right printed


class Solution:
    def inorderTraversal(self, root) :
        
        st=[]
        st.append(root)
        
        res=[]
        
        while st:
            Node=st.pop()
            if Node:
               res.append(Node.val)
               st.append(Node.right)
               st.append(Node.left)
          
             
            
        return res