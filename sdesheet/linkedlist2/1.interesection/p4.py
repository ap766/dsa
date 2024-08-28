#They ultimately get aligned .


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def getIntersectionNode(self, headA, headB):
        temp1=headA
        temp2=headB
        
        while temp1!=temp2:
            if temp1 is not None:
                temp1=temp1.next
            else:
                temp1=headB
                
            if temp2 is not None:
                temp2=temp2.next
            else:
                temp2=headA
                
        return temp1