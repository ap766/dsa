# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        dummynode = ListNode(-1)
        temp = dummynode
        carry = 0
        
        while l1 is not None or l2 is not None or carry:
            sum = 0  # Reset sum at the beginning of each iteration
            
            if l1 is not None:
                sum += l1.val
                l1 = l1.next  # Advance l1 pointer
            if l2 is not None:
                sum += l2.val
                l2 = l2.next  # Advance l2 pointer
                
            sum += carry
            carry = sum // 10
            
            node = ListNode(sum % 10)
            
            temp.next = node
            temp = temp.next
        
        return dummynode.next
    

#BELOW IS WITHOUT THE DUMMY NODE
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = None
#         tail = None
#         carry = 0
        
#         while l1 is not None or l2 is not None or carry:
#             sum = 0
#             if l1 is not None:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2 is not None:
#                 sum += l2.val
#                 l2 = l2.next
#             sum += carry
#             carry = sum // 10
#             node = ListNode(sum % 10)
            
#             if head is None:
#                 head = node
#                 tail = node
#             else:
#                 tail.next = node
#                 tail = tail.next
        
#         return head