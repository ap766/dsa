#Kadane's Algorithm.
#1.So if we carry negative sum, the sum will always reduce , so if we take less than 0 we can jus t take zero
class Solution:
    def maxSubArray(self, nums) -> int:
        max=-10**4-1
        sum=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            

            if (sum>max):
                max=sum
                
            if (sum<0):
                sum=0
            
        
            
        return max
            

#WHENVER WE ARE STARTING TO FORM A NEW SUBARRAY ITS FROM ZERO SO MARK THAT INDEX AS START


class Solution2:
    def maxSubArray(self, nums) -> int:
        max=-10**4-1
        sum=0

        ansstart=-1
        ansend=-1
        start=0

        for i in range(0,len(nums)):

            if sum==0:
               start=i
            sum=sum+nums[i]
            

            if (sum>max):
                max=sum
                ansstart=start
                ansend=i
                
            if (sum<0):
                sum=0
            

        
        print(nums[ansstart:ansend+1])
        return max
    
s2=Solution2()
print(s2.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
            

#INTERVIEW

#1)So maybe in one traversal to reduce to reduce the time complexity.
#2)So maybe we observe when the sum can no longer be our answer maybe when its negative and we reset it
#3)But for negative so just reverse it.


#FOR ME - THINK KADANE'S The idea of the Kadane’s algorithm is to find the maximum sum using one traversal of the array from left to right