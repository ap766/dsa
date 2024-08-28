# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int) :
        if head == None or head.next == None:
          return head  
    
        for i in range(0,k): #for all the rotations that can happen
            temp=head
            while temp.next.next!=None:
                  temp=temp.next #so temp is storing the second last none.
                    
            end=temp.next #the ending node
            
            #Make it last
            temp.next=None #Becuase that will be last
            
            #Making it head
            end.next=head
            head=end
            
        return head
            