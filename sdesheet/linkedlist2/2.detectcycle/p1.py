
# Node class represents
# a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to detect a loop 
# n a linked list
def detect_loop(head):
    # Initialize a pointer 'temp' at 
    # the head of the linked list
    temp = head

    # Create a set to keep track
    # of encountered nodes
    node_set = set()

    # Step 2: Traverse the linked list
    while temp is not None:
        # If the node is already
        # in the set, there is a loop
        if temp in node_set:
            return True

        # Store the current node in the set
        node_set.add(temp)

        # Move to the next node
        temp = temp.next

    # Step 3: If the list is successfully
    # traversed without a loop, return False
    return False

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_loop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    # No need to explicitly free memory
    # in Python; memory management is automatic


