#"The intuition behind the algorithm is to use 
# three pointers to segregate the array into three sections: 
# one for each category. By using these pointers, we can ensure 
# that each element is placed in its correct position with minimal swaps."

# #Time Complexity: O(N), where N = size of the array. We are iterating through the array only once.
# #Space Complexity: O(1) as we are not using any extra space.


#1)arr[0….low-1] contains 0. [Extreme left part]
# arr[low….mid-1] contains 1.
# arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
# The middle part i.e. arr[mid….high] is the unsorted segment. So, hypothetically the array with different markers will look like the following:

#2)In our case, we can assume that the entire given array is unsorted and so we will 
#place the pointers accordingly. For example, if 
#the given array is: [2,0,2,1,1,0], the array with the 3 pointers
# will look like the following:

#Here, as the entire array is unsorted, we have placed the mid pointer in the first
#  index and the high pointer in the last index. The low is also pointing to the first 
# index as we have no other index before 0. Here, we are mostly interested in placing 
# the ‘mid’ pointer and the ‘high’ pointer as they represent the unsorted part 
# in the hypothetical array.

#3)tHE SWAPPING.

class Solution:
    def sortColors(self, arr) -> None:
        
     low=0
     mid=0
     high=len(arr)-1
        
     while mid<=high:
        
        if arr[mid]==0:
          arr[low],arr[mid]=arr[mid],arr[low]
          low+=1
          mid+=1
        
        elif arr[mid]==1:
           mid+=1
            
        elif arr[mid]==2:
           arr[mid],arr[high]=arr[high],arr[mid]
           high-=1 
            
    
        
        
    

