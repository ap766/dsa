


def maxProductSubArray(nums):
    result = nums[0]
    for i in range(len(nums) - 1):
        p = 1
        for j in range(i, len(nums)):
            p *= nums[j]
            result = max(result, p)
       
    return result

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))


#O(N^2
