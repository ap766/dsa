#1.First Imagine if there were 2 linked list then how would you solve
 #It is similar to merging the 2 sorted linkedlist into one.
#We create a dummy node and assign it to temporary and res, cus we wanna keep a track of it so 2 nodes.
#Do not move res it helps u get the head back once your have got the entire flattened link list

#2.Bottom pointer pointer of res points to the head and 19's next can be made to point to null//

#3.Last 2 into 1.Again the last 2 and so on.

#4.We use recursion.Flatten(l1) Again Flatten(l2) and Flatten(L3) and then Flatten(L4).The moment we reach last node that the base code for our node.
#We return l4 node. And before returning call a merge function(l3 and l4) gives l5.Again mrge between l2 and l5 this gives l6 

#Time complexity. - O(Sumation)
#Space complexity - O(1) 


class Node:
    def __init__(self, data):
        self.data = data
        self.bottom = None
        self.next = None

class Solution:
    
    def merge(self, l1, l2):
        dummy = Node(-1)
        temp = dummy
        
        while l1 and l2:
            if l1.data < l2.data:
                temp.bottom = l1
                l1 = l1.bottom
            else:
                temp.bottom = l2
                l2 = l2.bottom
            temp = temp.bottom
        
        if l1:
            temp.bottom = l1
        else:
            temp.bottom = l2
        
        return dummy.bottom
                
    def flatten(self, root):
        if root is None or root.next is None:
            return root
            
        root.next = self.flatten(root.next)
        root = self.merge(root, root.next)
        
        return root

#Here dummy instead of res.