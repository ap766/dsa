#Observation Based
#1. If all are positive we can just take all the elements of the array
#Even negatives also multiply all.

#2. odd nah , so we observe if we ignore one minus , so whatever we take is prefix or suffix.
#And yeah the one on the middle will obviously not be the final answer
#And so yeah max preffix and suffix

#3.CASE of Zero So, we will divide the given array based on the location of the 0’s 

# ..............
# #CODE

#So for the other numbers just maintain a INT MAX - HeY mAyBe iT dOeSnT nEeD tO Go TiLl tHe EnD?- but its like bleh how much tc will we even reduce by this?
#And for the zeros just TURN IT TO 1 whenver you come accross it 

# #[-2,0,-1]  if nums[i] == 0:
#                 pre = 1
#             else:
#                 pre *= nums[i]
#Something like wont work.

class Solution:
    def maxProduct(self, nums) -> int:
        pre=1
        suf=1
        maxval=float('-inf')
        for i in range(0,len(nums)):
            
            if pre==0:
                pre=1
            if suf==0:
                suf=1
                
            pre*=nums[i]
            suf*=nums[len(nums)-1-i]
            
            maxval=max(maxval,max(pre,suf))
        return maxval
            
        
        
                
