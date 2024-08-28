from sys import *
from collections import *
from math import *


def getLongestSubarray(a, k: int) -> int:
    l = 0
    r = 0
    n = len(a)
    maxlen = 0
    sum = 0

    #We cant just use sum directly cus sum stores from the very beginning only.
    while r < n:
        sum += a[r]
        print(sum)
        while l < r and sum > k:
            sum -= a[l]
            l += 1

        if sum == k:
            maxlen = max(maxlen, r - l + 1)

        r += 1
    return maxlen
        

#-1 0 1 1 -1 -1 0
ans=getLongestSubarray([-1,0,1,1,-1,-1,0],0)
print(ans)