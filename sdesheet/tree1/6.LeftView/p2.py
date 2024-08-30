#SC at the worse case is all the nodes at the bottom which maybe half of the nodes which is a lot apparently.

#But for recursive TC=O(N) SC=O(H) H is the height (so ig this would make a huge difference in certain cases?)
#One might argue that skew trees it would be O(N) , Well whatever waht we are talking about here anyways is recursive stack space.

#So well we wont do iterative we will do Recursive and 

#Right Side View 

#1)We will follow reverse preorder traversal. - R Ri L, Because then first node we get will be the right one.
#2)Recursive Function - Pass Node and level. Node is the starting point point or root of the tree intially. 
#3)Basically we have a ds we keep comparising size and adding if its reached a size means it has a element aleady in it
   
#Function to return a list containing elements of left view of the binary tree.

def LeftView(root):
    ds=[]
    def recur(node,level):
        
        if node is None:
            return
        
        if (level == len(ds)):
            ds.append(node.data)
            
        recur(node.left,level+1)
        recur(node.right,level+1)
        
    recur(root,0)  
    return ds
