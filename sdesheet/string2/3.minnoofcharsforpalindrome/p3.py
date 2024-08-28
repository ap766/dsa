class Solution:
    # @param A : string
    # @return an integer
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
        
        
    def solve(self, pattern):
        lps=self.create_lps(pattern+"$"+pattern[::-1])
        print(lps)
        return len(pattern)-lps[-1]
    

# Sample testcases
s = Solution()
print(s.solve("ABC"))