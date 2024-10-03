class Solution:
    def longestOnes(self, nums, k: int) -> int:
        #1110011110
        #1110011110
        maxsum=0
        m=0#zeros count
        for i in range(0,len(nums)):
            m=0
            sum=0
            for j in range(i,len(nums)):
                if (nums[j]==1)or (nums[j]==0 and m<k):
                
                   if nums[j]==0:
                      m=m+1
                   sum+=1
                 
                  
                   maxsum=max(sum,maxsum)
                 
                else:
                    break
        return maxsum