#Slow - fast pointer method extenstion and 2 parts.
#1)Find the collision point
#MOve slow by 1 step
#MOve Fast by 2 steps

#So they collide at a given node - y check detect cycle

#2)Starting pt
#So we put a entry pointer at the start of the linked list.
#Move the entry and slow simulatenously till they dont collide and eventuallly they collide that is the startung point.

#If no cycle 
#Fast pointer will reach null no collision point.
 
##INTUITION
#L2 is the distance that would have been travelled by the slow pointer from the starting(yes couple of cycles possible.)
#SLOW POINTER => L1 + L2
#FAST POINTER => L1 + L2 + nC AND( EXTRA TURNS ALSO N TURNS MAYBE.)

#WE KNOW FAST POINTER TRAVELS TWICE OF SLOW POINTER.
#2(l1+l2)=l1+l2+nC
# l1+l2=Nc
# l1=nC-l2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
    
#SO IN THE CODE INSTEAD OF MAKING USE OF NEW ENTRY POINTER WE USE SLOW ITSELF AND FAST IS USED IN PLACE OF SLOW(I MEAN ANYWAYS THEY MEET AT THE SAME PT)