#1)Make use of 2 pointers.Cur is used to point to the
# first node which also head points to.

#2)The prev will be initially set to null.

#3)So for the first node we are going to take the next pointer and reverse it.So now the next pointer
#is pointing at null(prev).So this is going to be our last element in the new reversed linked list.


#4)Now we can shift our pointers.So we take prev pointer and shift it to current 
#and current pointer to the next node.
#(WE NEED TO SAVE THE LINK THAT WE BROKE.

#5)When cur is zero , prev returned as new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        cur=head
        prev=None
        
        while cur is not None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            
            
        return prev
        
            