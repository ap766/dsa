def maxSubarraySum(nums, n):
    max_sum = -10**6-1
    for i in range(0, len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
           
                print(nums[j])
                current_sum += nums[j]
                if current_sum > max_sum:
                   max_sum = current_sum



    if max_sum<0:
                return 0

    return max_sum



arr=[18,-6,-6,-5,7,10,16,-6,-2,0] 
n=len(arr)
print(maxSubarraySum(arr, n))
