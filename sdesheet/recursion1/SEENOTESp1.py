from typing import List

def subset(i: int, s: List[int],sum: int,  result: List[int]) -> None:


    #i is the index of the current element
    #num is the input array
    #sum is the sum of the current subset
    #ans is the vector that contains all the subset sums

    # Completely traverse the whole array, insert the "sum" in the "ans" vector.
    if i == len(s):
        result.append(sum)
        return

    # Insert the element in the sum.
    subset(i + 1, s,sum + s[i],result)

    # Don't take the element in the sum.
    subset(i + 1,s,sum, result)


def subsetSum(num: List[int]) -> List[int]:

    # Ans vector contains all the subset sums.
    result = []

    
    subset(0,num, 0, result)
    
    # Sort the vector and finally return it.
    print(result)
    result.sort()
    return result

# Driver Code
print(subsetSum([3, 1,2]))