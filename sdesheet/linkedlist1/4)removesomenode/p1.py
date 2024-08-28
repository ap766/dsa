# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, N: int):
         
        cnt=0
        temp=head
        while temp is not None:
            cnt+=1
            temp=temp.next
        
        if cnt==N: 
            headNode=head.next
            head=None
            return headNode 
        res=cnt-N#Before the node we wanna delete 
        
        temp=head
        while temp is not None:
            res-=1
            if res==0:
                break
       
            temp=temp.next #Yeah so of course we have the doubt as to how we can even get 3 if it breaks before but thats cus its already assigned to head girlll so 1st node done
            
        delNode=temp.next
        temp.next=temp.next.next
        delNode=None
        
        return head