def twoSum( nums, target):
    numMap = {}

    for i in range(0,len(nums)):
      
        numMap[nums[i]] = i

    for i in range(0,len(nums)):
        complement = target - nums[i]
        print(complement)
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []

print(twoSum([2,7,11,15],9))

