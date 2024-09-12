#1)Just iterate thru linked lists and store in an array
#2)And then sort it
#3)So we want the head of the combined linked list , so rn we have an array we'll convert to ll


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
    

# Time Complexity: O(N1 + N2) + O(N log N) + O(N) where N1 is the number of linked list nodes in the first list and N2 is the number of linked list nodes in the second list and N is the total number of nodes (N1+N2). Traversing both lists into the array owes O(N1 + N2), sorting the array takes O((N1+N2)*log(N1+N2)) and then traversing the sorted array and creating a list gives us another O(N1+N2).

# Space Complexity : O(N)+O(N) where N is the total number of nodes from both lists, N1 + N2. O(N) to store all the nodes of both the lists in an external array and another O(N) to create a new combined list.Time Complexity: O(N1 + N2) + O(N log N) + O(N) where N1 is the number of linked list nodes in the first list and N2 is the number of linked list nodes in the second list and N is the total number of nodes (N1+N2). Traversing both lists into the array owes O(N1 + N2), sorting the array takes O((N1+N2)*log(N1+N2)) and then traversing the sorted array and creating a list gives us another O(N1+N2).

# Space Complexity : O(N)+O(N) where N is the total number of nodes from both lists, N1 + N2. O(N) to store all the nodes of both the lists in an external array and another O(N) to create a new combined list.