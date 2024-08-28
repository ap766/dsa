def twoSum( nums, target):
    numMap = {}

    for i, num in enumerate(nums):
      

        numMap[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        print(complement)
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []

print(twoSum([2,7,11,15],9))

