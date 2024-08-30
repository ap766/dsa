#Algorithm - We have observed that slow pointer can move 1 and fast pointer reaches the end then (for odd)


#FAST AND(FAST.NEXT MEANS ITS NOT LAST POINTER )
#SO FOR EVEN - IT WILL GO TO THE LAST POINTER WHEN THE SLOW IS AT MID
#FOR ODD-IT WILL GO OUT OF BOUNDS WHEN THE SLOW IS AT MID

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        fast=head
        slow=head
        
        #So for odd it will check the fast.next is next (so goes till last)
        #but for even it will become null 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            
        return slow