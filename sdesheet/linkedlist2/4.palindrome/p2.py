#1) So we take slow and fast pointer and we move fast till 2nd last(even) or last(odd) node.
# For even , we take the left as middle. The slow pointer is at the first middle.#We reverse the 
# second half of the linked list.

#2)We move slow by 1. And we take one more dummy node and place it at the head of the linked listt.
#Start traversing both these nodes simultaneously. Again move it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev #prev is the new head

    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the list
        second_half = self.reverseList(slow)
        
        # Compare the first half and the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
        