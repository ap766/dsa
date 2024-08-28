#1)Recursion so the first function we go top down (basically till the array is empty) we keep poping 
#2)An the second fucntion we keep sorting down to top
#3)Now the sorting down to top may have a if else based on if the topmost or not (here also recursion takes place becuase the elements large are poped off and stored in  elment.)



#Use recursion 
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def SortedInsert(self,s,ele):
        if len(s)==0 or ele>s[-1]:
           s.append(ele)
        else:
           a=s.pop()
           self.SortedInsert(s,ele)
           s.append(a)
           
    def Sorted(self, s):
        # Code here
        if len(s)!=0:
            ele=s.pop()
            self.Sorted(s)
            self.SortedInsert(s,ele)
            
