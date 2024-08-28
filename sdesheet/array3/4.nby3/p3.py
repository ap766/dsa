#In the Boyer-Moore Voting Algorithm, we are trying to find the majority element(s) that appear more than ⌊N/3⌋ times. The reason we look for two elements is that, in any array, there can be at most two elements that appear more than ⌊N/3⌋ times. This is because if there were three or more such elements, their total count would exceed N, which is impossible.

#Then rest is the previous q's intuition

class Solution(object):
    def majorityElement(self, nums):
        cnt1, cnt2 = 0, 0
        n = len(nums)
        ele1, ele2 = float('-inf'), float('-inf')
        
        for i in range(n):
            if cnt1 == 0 and nums[i] != ele2:
                cnt1 = 1
                ele1 = nums[i]
            elif cnt2 == 0 and nums[i] != ele1:
                cnt2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        ls = []
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == ele1:
                cnt1 += 1
            if nums[i] == ele2:
                cnt2 += 1
                
        if cnt1 > n // 3:
            ls.append(ele1)
        if cnt2 > n // 3:
            ls.append(ele2)
            
        ls.sort()
        return ls