class Solution:
    def getIntersectionNode(self, headA, headB):
        while headB is not None:
            temp = headA
            
            while temp is not None:
                # if both nodes are same
                if temp == headB:
                    return headB
                temp = temp.next
                
            headB = headB.next
        # intersection is not present between the lists
        return None


# Time complexity: O(n*m)