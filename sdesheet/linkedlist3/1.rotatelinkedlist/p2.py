# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int) :
        if not head or k == 0:
            return head
        
        # Count the length of the list
        temp = head
        cnt = 1
        while temp.next is not None:
            cnt += 1
            temp = temp.next
        
        # Make the list circular
        temp.next = head
        
        # Find the new tail: (cnt - k % cnt - 1)th node
        k = k % cnt
        steps_to_new_head = cnt - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        # Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head