#Initially initialise a left pointer at 0 and right pointer at n-1
#intially total water/res is 0 becuase we have no water
#We keep the leftmax as 0
#We keep the rightmax as 0
#We check if the value at a[l]<=a[r]
#If yes We then compare if the 0 at a[l] is greater than at leftmax if it is then no water stored
#So leftmax stays as zero and we increase l++
#Now again when we check the value is greater than leftmax so make leftmax as 1
#So condition is a[i]>=leftmax then update the leftmax to a[i]
#If leftmax is not zero and a[i] is less than leftmax there can be a unit of water stored
class Solution:
    def trap(self, a) -> int:
        n=len(a)
        leftmax=0
        l=0
        rightmax=0
        r=n-1
        res=0
        
        while l<r:
            if a[l]<=a[r]:     
              if a[l]>=leftmax:
                 leftmax=a[l] #And this left max could actually be more than a[r] so we dont do it
              else:
                 res+=(leftmax-a[l])
              l+=1

            else:
              if a[r]>=rightmax:
                 rightmax=a[r]
              else:
                 res+=(rightmax-a[r])
              r-=1
                
        return res
    



# Intuition: We need a minimum of leftMax and rightMax.So if we take the case when height[l]<=height[r] we increase l++, so we can surely say that there is a block with a height more than height[l] to the right of l. And for the same reason when height[r]<=height[l] we can surely say that there is a block to the left of r which is at least of height[r]. So by traversing these cases and using two pointers approach the time complexity can be decreased without using extra space.