from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev = nums[0]
        ct = 1
        k = 1
        
        for i in range(1, len(nums)):
            if prev != nums[i]:
                prev = nums[i]
                nums[k] = prev
                k += 1
                ct += 1
        
        return ct


#So like according to striver its nlogn + n but python see imge
















#OR-----









#2 pointers - we go check which element is not equivalent.And
#We put it in the next index.

#So we have a pointer k as i and i as j


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Start from the second position
        ct = 1  # Count the first element as unique
        
        for i in range(1, len(nums)):
            if nums[k - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
                ct += 1
        
        return ct

#k is to compare and then replace 



#2 pointers
#i says You can take the space in front of me and i will pt to you.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1