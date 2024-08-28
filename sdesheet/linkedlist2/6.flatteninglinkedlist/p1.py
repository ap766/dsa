#Using Array

                                
class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

def convertArrToLinkedList(arr):
  
    dummyNode = Node(-1)
    temp = dummyNode


    for val in arr:
        temp.child = Node(val)
        temp = temp.child

    return dummyNode.child

def flattenLinkedList(head):
    arr = []

    while head:
        t2 = head
        while t2:
            arr.append(t2.data)
            t2 = t2.child
        head = head.next

    arr.sort()
    return convertArrToLinkedList(arr)


def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()


def printOriginalLinkedList(head, depth=0):
    while head:
        print(head.data, end="")

    
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        if head.next:
            print()
            print("| " * depth, end="")

        head = head.next

head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)


print("Original linked list:")
printOriginalLinkedList(head)

flattened = flattenLinkedList(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)
                                
                            