#So if we have an asterisk it can either go to -1 , 0 or 1,so we will try to carry a range. min initially is zero and maximum initially is zero.

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                min_open += 1
                max_open += 1
            elif s[i] == ')':
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            
            if max_open < 0:
                return False
            if min_open < 0:
                min_open = 0
        
        return min_open == 0

