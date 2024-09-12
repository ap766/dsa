# Generate Parenthesis 

# #1)So maybe we can go with a brute-force approach. So first of what i am thinking what does n tell us about valid parenthesis. So first 3 open and 3 close parenthesis.But  what about the order of parenthesis.(I want to anylyse the order of parenthesis)
# #2)Okay so can be start out with closed parenthesis - No we know its invalid no matter what what always mess it up.
# #3)So we always start with open parenthesis. Okay now lets say we have one open parentheses can we have another open parenthesis yess because our 3 is 3 so we are allowed, what about a closing - yes yes cus close is 0 anyways just increases to 1.Another open yes cus limit 3 we have only 1 , what about closing no cus we have 1 pair already the closing parenthesis wont have a matching open parenthesis on the left of it. 
# #4)So we can track open and close so we can only add close parentheses if count of clois less than open.
# #5)So our base case would be we have 3 open and 3 closed parenthesis and the condition tells us when we can add more open parenthesis.




# #1)So we start  with a open 












class Solution:
    def generateParenthesis(self, n: int):
        ans=[]
        
        def recur(opend,closed,current):
            if opend==closed==n:
                ans.append(current)
                
                
            if opend<n:
                recur(opend+1,closed,current+"(")
            if closed<opend:
                recur(opend,closed+1,current+")")
            
            
        recur(0,0,"")
        return ans
            

#  def recur(opend,closed,current):
#             if len(current)==2*n:
#                 ans.append(current)

#WILL ALSO WORK
        