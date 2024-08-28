# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head) :
         temp = head
         node_map={}
         while temp is not None:
                if temp in node_map:
                    return temp
                node_map[temp]=True
                temp=temp.next
         return None