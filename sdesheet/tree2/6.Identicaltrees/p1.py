# To determine if two binary trees are identical, we can follow a recursive approach. We traverse both trees in the preorder manner, meaning that the current node's value is checked before recursively traversing its left and right subtrees.

class Solution:
    def isSameTree(self, p, q) -> bool:
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))