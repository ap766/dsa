
# left records the number of ( we need to add on the left of S.
# right records the number of ) we need to add on the right of S,
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        
        left = right = 0
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                if i == '(':
                   right +=1 
                else:
                   right -=1
        return left + right
    
    