#So basically we can make use of a stack to keep stack of the nodes
#We can use cur to point to the curretn node
#If this cur is None it implies its reached the end of the tranversal - left or right
#So at first we traverse the left subtree 
#And if it is is None we print the root 
#Then we traverse the right subtree


class Solution:
    def inorderTraversal(self, root):
        st=[]
        cur=root
        ans=[]
        
        while True:
            if cur is not None:
                st.append(cur)
                cur=cur.left
            elif st:
                cur=st.pop()
                ans.append(cur.val)
                cur=cur.right     
            else:
                break
                
        return ans