from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.

    n=len(arr)
    x=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]

    arr[n-1]=x

    return arr

