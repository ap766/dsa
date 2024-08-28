#A dummy node whose next points to 1
#A prev node which points to dummy(does pre also pt to 1? loks like yes)
#A cur node which points to 1
#A nex node - dummy node pointing to next of cur

#.........................................

#So we use the prev.next to point to the prev node
#We use the cur.next to point to the next node
#nex is current thing that changes at the end cus of course we have to go to the follwoing

#Like now we are operating on 2
#So first cur.next=nex.next
#Where the bond is changed nex.next=prev.next(2's next pointing to 1 now)
#Then prev.next=nex
#Then nex=cur.next

#...........................

#Next we make prev to point to cur 
#then cur should point to prev's next which is 4
#SO cur is always standing at the first of any group
#ANd make nex point to the 2nd which is actually the currently bcus 4's pointing will be in the last again
#And so the 1->6 also happens thru prev.next cus its 1's next

#DUMMY NODE 's next to 3 which is head 

#.........................................

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        count = 0
        cur = dummy
        pre = dummy
        nex = dummy
        
        while cur.next:
            cur = cur.next
            count += 1
        
        while count >= k:
            cur = pre.next
            nex = cur.next
            for i in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k
        
        return dummy.next
