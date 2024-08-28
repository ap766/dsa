# The naive approach is pretty straightforward. We will use nested loops 
# to solve this problem. We know index i must be smaller than index j. So, 
# we will fix i at one index at a time through a loop, and with another loop, 
# we will check(the condition a[i] > a[j]) the elements from index i+1 to N-1 
# if they can form a pair with a[i]. This is the first naive approach we can think of.


from typing import List

def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print("The number of inversions is:", cnt)

