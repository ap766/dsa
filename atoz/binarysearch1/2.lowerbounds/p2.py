#Is it always found , if not what should it return

#intuition - since its sorted its binary search

#implementation:

#1.We can make use of two pointers left and right to define the search space.
#2.now we calculate mid and if we already find an answer we will try to find a smaller 
#index by elminating the right half.
#3.however if we dont have an answer and the value is smaller than x then So, we will eliminate the left half and search in the
# right half for the answer.



def lowerBound(arr, n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

