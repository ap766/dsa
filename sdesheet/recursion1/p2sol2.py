#

def findSubsets(ind,ds):
            
            ans.append(ds[:])
            for i in range(ind, len(nums)):
          
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                
                findSubsets(i + 1,ds+[nums[i]])
                
ans = []
ds = []
nums=[1,2,2,2,3,3]
nums.sort()
findSubsets(0,[])
print(ans)




