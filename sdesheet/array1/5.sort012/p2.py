#Intuition: Since in this case there are only 3 distinct values in the array
#so it's easy to maintain the count of all, Like the count of 0,
#1, and 2. This can be followed by overwriting the array based on the
#frequency(count) of the values.

#Time Complexity: O(N) + O(N), where N = size of the array. First O(N) for counting the number of 0’s, 1’s, 2’s,
# and second O(N) for placing them correctly in the original array.
# Space Complexity: O(1) as we are not using any extra space.

class Solution:
    def sortColors(self, nums) -> None:
         
        one=0
        zero=0
        two=0
        
        for i in range(0,len(nums)):
            if nums[i]==0:
                zero+=1
            elif nums[i]==1:
                one+=1
            elif nums[i]==2:
                two+=1
                
        for i in range(0,zero):
            nums[i]=0
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,len(nums)):
            nums[i]=2
            