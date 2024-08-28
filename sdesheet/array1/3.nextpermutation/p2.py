#1.We observe what happens in a dictionary that elements are close to each other tend
#to have longer prefixes that are common.So based on this for our example we are looking for longing prefix match.

#2.So we try to look for long prefix match but we will leave some stuff to rearrage
#and get next one , but if the left over is in descending order we cant just 
#get it from arraging those. So the prefix match is made shorter accordingly.

#3.So if its not in descending we can thing of getting the next oneusing these
#lefovers.So we want the right away next greater . 

#4.So for this Find the break-point, i: Break-point means the first index i from the back of the given array where arr[i] becomes smaller than arr[i+1].
#But breakpoint is basically to find the longest prefix

#5.So from the end we try to find the number that is greater than it 

#6.the rest we can just reverse to get the smallest after ind(break pt)

#..........................................................................
#CODE
#Okay

#1.So n-2 can be the last dip/breakpoint , it starts from here

#Time Complexity
#Time Complexity: O(3N), where N = size of the given array
# Finding the break-point, finding the next greater element, and reversal at the end takes O(N) for each, where N is the number of elements in the input array. This sums up to 3*O(N) which is approximately O(3N).

class Solution:
    def nextPermutation(self, nums) -> None:
        
        n=len(nums)
        ind=-1 #breakpoint
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
                
        if ind==-1:
           nums.reverse()
           return nums
        
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
                
        nums[ind+1:]=reversed(nums[ind+1:])
        
        return nums
        
            
            
        