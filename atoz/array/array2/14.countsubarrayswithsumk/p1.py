class Solution:
    def subarraySum(self, nums, k: int) -> int:
        h = {}
        h[0] = 1 #So this is for the stuff thats from the start of Array .
        sum = 0
        cnt = 0
        for i in range(len(nums)):
            sum += nums[i]
            remove = sum - k
            if remove in h:
                cnt += h[remove]
            if sum in h:
                h[sum] += 1
            else:
                h[sum] = 1
        return cnt
           