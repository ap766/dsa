class Solution:
    def fourSum(self, nums,target):
        nums.sort()
        ans=[]
        for i in range(0,len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
                
            for j in range(i+1,len(nums)):
                    if j>i+1 and nums[j]==nums[j-1]:
                        continue
                    
                    k=j+1
                    l=len(nums)-1
                    
                    while k<l:
                        
                        total_sum=nums[i]+nums[j]+nums[k]+nums[l]
                        
                        if total_sum<target:
                            k=k+1
                        elif total_sum>target:
                            l-=1
                        else:
                            ans.append([nums[i],nums[j],nums[k],nums[l]])
                            k+=1
                            l-=1
                            
                            while k<l and nums[k]==nums[k-1]:
                                k+=1
                                
                            while k<l and nums[k]==nums[l+1]:
                                l-=1
                                
        return ans