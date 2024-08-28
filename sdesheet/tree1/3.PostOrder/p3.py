# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        st = []
        postorder = []
        cur = root
        
        #How exactly this cur and st works.
        while cur is not None or st:
            if cur is not None:
                st.append(cur)
                cur = cur.left
            else:
                temp = st[-1].right
                if temp is None:
                    temp = st.pop()
                    postorder.append(temp.val)

                    #$What this part exactly means
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        postorder.append(temp.val)
                else:
                    cur = temp
        
        return postorder