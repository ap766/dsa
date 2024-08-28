# # Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def convert_array_to_listedlist(self, arr):
#         dummy_node = ListNode(-1)
#         temp = dummy_node
        
#         for i in range(len(arr)):
#             temp.next = ListNode(arr[i])
#             temp = temp.next
#         return dummy_node.next
    
            if not arr:
                return None

            head = ListNode(arr[0])
            temp = head

            for i in range(1, len(arr)):
                temp.next = ListNode(arr[i])
                temp = temp.next
            return head
        
    def mergeTwoLists(self, list1,list2):
        arr = []
        temp1 = list1
        temp2 = list2
        
        while temp1 is not None:
            arr.append(temp1.val)
            temp1 = temp1.next
            
        while temp2 is not None:
            arr.append(temp2.val)
            temp2 = temp2.next
            
        arr.sort()
        
        head = self.convert_array_to_listedlist(arr)
        return head