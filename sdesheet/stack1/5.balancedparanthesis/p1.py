class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                else:
             

                    a=st.pop()

                    if a=='(' and s[i]==')' or a=='[' and s[i]==']' or a=='{'and s[i]=='}':
                        pass
                    else:
                        return False
        if len(st)==0:
                return True
        else:
                return False
                        