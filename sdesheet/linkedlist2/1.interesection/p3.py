# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDifference(self, headA, headB):
        len1 = 0
        len2 = 0
        tempA = headA
        tempB = headB
        while tempA is not None or tempB is not None:
            if tempA is not None:
                len1 += 1
                tempA = tempA.next
            if tempB is not None:
                len2 += 1
                tempB = tempB.next
        return len1 - len2

    def getIntersectionNode(self, headA, headB):
        diff = self.getDifference(headA, headB)
        if diff < 0:
            while diff != 0:
                headB = headB.next
                diff += 1
        else:
            while diff != 0:
                headA = headA.next
                diff -= 1

        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None