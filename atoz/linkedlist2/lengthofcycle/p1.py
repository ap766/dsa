#So basically this can also be done by using a map and having key value pair of node and timer
#The map approach maybe beter cus only one while loop.

#My approach is also the first approach in gfg
#O(N) - TC
#O(N) - SC

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        s = set()
        temp = head
        c = 0
        
        while temp is not None:
            if temp in s:
                loop_node = temp  # The node where the loop starts
                break
            s.add(temp)
            temp = temp.next
            
        # If a loop is detected
        if temp is not None:
            temp = temp.next
            c = 1
            while temp != loop_node:
                c += 1
                temp = temp.next

        return c if c > 0 else 0
