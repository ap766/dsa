class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l=0
        r=0
        n=len(nums)
        maxlen=0
        zeros=0
        
        while r<n:
            if nums[r]==0:
                zeros+=1
            
            if zeros>k:
                if nums[l]==0:
                   zeros-=1
                l+=1
                
            if zeros<=k:   
               maxlen=max(maxlen,r-l+1)
            r+=1
                
        return maxlen