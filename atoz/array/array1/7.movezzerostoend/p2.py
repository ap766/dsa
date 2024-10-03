class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #so we have a right pointer whose job is to move elements to the left.
        #we dont do anything if its a zero but if its a non zero we swap to the left
        
        #so now once we have put a value at the left(thru swapping) we wanna shift left pointer  
        
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums
    

    