#1)WE TRY TO REMOVE THE LINKS. AND REVERSE THEM . - When reversing a linked list, the main challenge is to reverse the links between the nodes while ensuring we do not lose access to the rest of the list during the process. Here's how the two-pointer approach naturally emerges as a solution:
# sO I THINK POINTERS COULD HELP US.


#2)
#SO WE CAN USE 2 POINTERS FOR THAT APPROACH WE USE CUR TO POINT TO THE CURRENT 
#AND WE CAN PREV TO POINT WHICH AT THE BEGINNING WE 

#1)Make use of 2 pointers.Cur is used to point to the
#first node which also head points to.

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



#INTUITION/APPROACH

#Okay so what i am thinking is we can remove the extra space required and we can just probably try to 
#reverse the direction of the arrows between eveynode and i think maybe using pointers would be a good idea to that
#So we have 2 pointers one to pt the current and another to point to the previous node and everytime we make te current's
#narrow poin to prevous'one's arrow and wwe would keep doing for the entire linked lsit
#ALGO



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
        
            