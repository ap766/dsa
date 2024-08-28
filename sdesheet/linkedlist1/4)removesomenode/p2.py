#1)We tried reaching right before (previous node) before . 2 steps lesser , to reach the previous node , we can do it without 
#knowing 5 is not required apparently.

#2)We take a fast pointer and move it 2 steps

#3)We take a slow pointer and now move it simultaneously
#with fast by 1 and the moment you reach the last node please stop.And 
#you see slowest Pointing to the previous.  Why cus we had moved fast already by N.

  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, N: int) :
         
         if head is None:
            return None
        
         fast=head
         slow=head
        
         #use for loop much easier
         for _ in range(0,N):
            fast=fast.next
            
         if fast is None: #That means head has to be removed.
            headnode=head.next
            head=None
            return headnode
            
                
         while fast.next: #ONce the next is none means we are done.We need to know it does reach none.
            fast=fast.next
            slow=slow.next
          
            
         delNode = slow.next
         slow.next = slow.next.next #do this before you delete.
         delNode = None
         return head