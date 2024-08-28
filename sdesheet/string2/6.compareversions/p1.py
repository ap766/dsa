class Solution:
    
    def compareVersion(self, version1: str, version2: str) -> int:
        
        i=0
        j=0
        m=len(version1)
        n=len(version2)
      
        while i<m or j<n:
            res1=0
            res2=0
        
            while i<m and version1[i]!='.':
                  res1=res1*10+int(version1[i])
                  i+=1
            i+=1
            
            while j<n and version2[j]!='.':
                  res2=res2*10+int(version2[j])
                  j+=1
            j+=1
            
            if res1>res2:
                return 1
            elif res1<res2:
                return -1
            
        return 0
    
#O(N) N IS THE LONGER STRING.