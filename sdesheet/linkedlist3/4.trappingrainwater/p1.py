class Solution:
    def trap(self, height) -> int:
        sum=0
        for i in range(0,len(height)):
            j=i
            n=len(height)
            maxleft=0
            maxright=0
            while j>=0:
                maxleft=max(maxleft,height[j])
                j-=1
            j=i
            while j<n:
                maxright=max(maxright,height[j])
                j+=1
                
            sum+=min(maxleft,maxright)-height[i]
            
        return sum
        