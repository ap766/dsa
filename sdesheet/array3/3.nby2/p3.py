class Solution:
    def majorityElement(self, arr) -> int:
        
        cnt=0
        ele=None
        n=len(arr)
        
        for i in range(n):
            if cnt==0:
               cnt=1
               ele=arr[i]
            elif ele==arr[i]:
                 cnt+=1
            else:
                cnt-=1
                
        for i in range(n):
            if arr[i]==ele:
                cnt+=1
                
        if cnt>(n//2):
            return ele
        
        return -1
    
#tc - o(n)
#sc - o(1)
    
