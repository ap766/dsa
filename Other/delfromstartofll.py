# https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/

# Python program to delete a linked list node at
# a given position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to delete a node at a given position


def deleteNode(head, position):
    # temp = head
    # prev = None

    # if temp is None:
    #     return head

    # # Case 1: Head is to be deleted
    # if position == 1:
    #     head = temp.next
    #     return head

    # # Case 2: Node to be deleted is in middle
    # # Traverse till given position
    # for i in range(1, position):
    #     prev = temp
    #     temp = temp.next
    #     if temp is None:
    #         print("Data not present")
    #         return head

    # # If given position is found, delete node
    # if temp is not None:
    #     prev.next = temp.next

    temp=head

    if position==1:
        newhead=temp.next
        head=None
        return newhead

    position-=1 #To get before 1 

    while temp is not None:
        position-=1
        if position==0: 
            break
        temp=temp.next
    
    deleteNode=temp.next
    temp.next=temp.next.next
    deleteNode=None

    return head

# Function to print the linked list


def printList(head):
    while head:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("None")


# Driver code
if __name__ == "__main__":
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Print original list
    print("Original list: ", end="")
    printList(head)

    # Deleting node at position 2
    position = 2
    head = deleteNode(head, position)

    # Print list after deletion
    print("List after deletion: ", end="")
    printList(head)
