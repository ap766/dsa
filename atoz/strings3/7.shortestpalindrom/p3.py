class Solution:
    def shortestPalindrome(self, pattern: str) -> str:
           
        lps=self.create_lps(pattern+"$"+pattern[::-1])
        add_length = len(pattern) - lps[-1]
        return pattern[::-1][:add_length] + pattern
        
    def create_lps(self,pattern):
            M=len(pattern)
            lps=[None]*M

            length=0
            lps[0]=length
            i=1

            while i<M:

                if pattern[i]==pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        

