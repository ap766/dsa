class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #2 pointers?
        i=0
        j=len(nums)-1



























        
        n=len(nums)
        cnt=0
        swaps=0
        
        for m in range(n):
            if nums[m]==0:
                cnt+=1
                
        i=n-cnt
        
        while i>0 and j>0:
            print(nums)
            if nums[i]==0: 
               nums[i]=nums[j]
               nums[j]=0
               i-=1
               j-=1
               swaps+=1
                
               if cnt==swaps:
                  break
            else:
               i-=1 
                
        print(nums)
        return nums
            
            
    
s=Solution()
s.moveZeroes([0,1,0,3,12])
            