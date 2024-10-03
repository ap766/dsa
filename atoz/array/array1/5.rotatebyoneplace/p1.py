from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.

    n=len(arr)
    temp=[0]*n
    for i in range(1,len(arr)):
        temp[i-1]=arr[i]

    temp[n-1]=arr[0]

    return temp
