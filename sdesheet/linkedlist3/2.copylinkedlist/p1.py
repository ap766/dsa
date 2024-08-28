#Can use the normal approach of using temp cus the nodes that random pointer points to are not created yet.



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        mpp = {}
        cur = head
        
        # First pass: create a copy of each node and store it in the hashmap
        while cur is not None:
            copy = Node(cur.val)
            mpp[cur] = copy
            cur = cur.next
        
        cur = head
        
        # Second pass: assign next and random pointers
        while cur is not None:
            copy = mpp[cur]
            copy.next = mpp.get(cur.next)
            copy.random = mpp.get(cur.random)
            cur = cur.next
        
        return mpp[head]
    
#2 PASSES ITS THE NEETCODE CODE.