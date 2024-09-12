
# Intuition: We will linearly travel the array. We can 
# maintain a minimum from the start of the array and compare 
# it with every element of the array, if it is greater than the 
# minimum then take the difference and maintain it in max, otherwise
#  update the minimum at every STAGE


#Approach
#Minimum cant be zero 


class Solution:
    def maxProfit(self, prices) -> int:
        
        minval=float('inf')
        maxprof=0
        for i in range(0,len(prices)):
            
            minval=min(minval,prices[i])
            maxprof=max(maxprof,prices[i]-minval)
            
        return maxprof
            
            
