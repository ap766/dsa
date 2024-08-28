
import math

def nCr(r, c):
    res = 1

    # calculating nCr:
    for i in range(c):
        res = res * (r - i)
        res = res // (c - i)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = pascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")
    


#tc is o(c)
#intuition is basically the formula