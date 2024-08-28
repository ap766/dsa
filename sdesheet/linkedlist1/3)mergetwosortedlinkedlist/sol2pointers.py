#1)Catch that our output list is empty this gives us
# a edge case cus we dont even have a list yet,common 
# techniqueto avoid the edge case of the initial empty list.

#2.So now we compare values and accordinging insert the node in the list .

#3.Now its possible that all the elements of one list are already traversed.
#So for the remaining portion is just added to the end.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_node = ListNode(-1)
        temp = dummy_node

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next  # Update temp inside the loop

        if list1 is not None:
            temp.next = list1

        if list2 is not None:
            temp.next = list2
         
        return dummy_node.next