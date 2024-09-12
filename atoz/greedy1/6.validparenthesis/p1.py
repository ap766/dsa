#so maybe we could Break the problem , Assuming simple problem of just brackets 
#Take a counter if add +1 if we encounter a opening and we do -1 if we encounter a closing bracket.So in a case
#where its (()()) it becomes a zero. And its proper.
#And we need think of ())(  in this case its not valid.
#So if the cnt goes less than 0 we can stop

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        def recur(s, ind, cnt):
            if cnt < 0:
                return False
            if ind == n:
                return cnt == 0
            
            if s[ind] == '(':
                return recur(s, ind + 1, cnt + 1)
            if s[ind] == ')':
                return recur(s, ind + 1, cnt - 1)
            
            return recur(s, ind + 1, cnt + 1) or recur(s, ind + 1, cnt - 1) or recur(s, ind + 1, cnt)
        
        return recur(s, 0, 0)
    
#Time complexity - 3^n
#Space complexity - n