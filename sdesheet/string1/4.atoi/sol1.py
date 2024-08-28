class Solution:
    def myAtoi(self, s: str) -> int:
        f=0
        sign="0"
        j=float("inf")
        for i in s:
            print(i)
          
            if i==' ' and (j==float("inf") or j==" "):
                print("a")
                continue
            if (i=='+' or i=='-') and sign in ['+','-']:
                print("b")
                if sign=="-":
                   f=-f
                return f
            if i=='-' and sign not in ['+','-'] and f==0:
                print("c")
                if j=="0":
                   return 0
                sign='-'
                continue
            if i=='+' and sign not in ['+','-'] and f==0:
                print("d")
                if j=="0":
                   return 0
                sign="+"
                continue
            
            if f==0 and i not in "0123456789":
                print("e")
                return 0
            if i not in "0123456789":
                print("f")
             
                if sign=="-":
                   f=-f
                return f
            
            f=f*10+int(i)
            j=i
       
     

        if sign=="-":
            f=-f
         
        if f>(2**31)-1:
           
            f=(2**31)-1
        if f<-2**31:
           
            f=-2**31
            
sol=Solution()
print(sol.myAtoi(" 42"))