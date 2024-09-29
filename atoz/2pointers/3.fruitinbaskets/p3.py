class Solution:
    def totalFruit(self, fruits) -> int:
        l=0
        r=0
        maxlen=0
        mpp={}
        n=len(fruits)
        while r<n:
         
            if fruits[r] in mpp:
                mpp[fruits[r]]+=1
            else:
                mpp[fruits[r]]=1
            
            if len(mpp)>2:
                mpp[fruits[l]]-=1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
           
                l+=1
                
            if len(mpp)<=2:
                maxlen=max(maxlen,r-l+1)
                
            r+=1
        return maxlen
