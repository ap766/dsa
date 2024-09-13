
#2 pointers 
class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        
        i=0
        j=0
        
        while i<len(g):
            
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                j+=1
                i+=1
            else:
                break
        return i
            