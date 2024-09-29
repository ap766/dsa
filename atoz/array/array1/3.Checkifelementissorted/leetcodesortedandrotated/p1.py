class Solution:
    def check(self, nums) -> bool:
        cnt=0
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                cnt+=1
        if nums[n-1]>nums[0]:
            cnt+=1
            
        if cnt<=1:
            return True
        else:
            return False
        
#So here its basically that if its sorted then last will greater than first or if rotated one place it breaks so either eay count is 1.
#However there is chance of 1 1 1 so we do the < thing