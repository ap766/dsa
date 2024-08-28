#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        
        slow=head
        fast=head
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                break
        else:
            # No loop detected
            return 0
        
        c=1    
        slow = slow.next #Instead of count 0 we do this cus then it will be equal right
        while slow!=fast:
            slow=slow.next
            c+=1
           
         
        return c