##INTUITION AND APPROACH
#1. I am thinking of storing all the elments somewhere and just reassigning them in a reversed manner
#2.SO one of the ways could just be using a array and remove the element from the end of the array  so we have another to keep track so 
#3.So i feel using a stack would be much with just pop operation and this way we reassign every node and done.


#ALGO

#1. we use a temporary variable as temp.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        st=[]

        temp=head 
        while temp is not None:
            st.append(temp.val) 
            temp=temp.next
            

        temp=head
        while temp is not None:
            temp.val=st.pop()
            temp=temp.next
            
        
        return head
        