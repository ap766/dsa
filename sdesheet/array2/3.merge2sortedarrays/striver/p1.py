# Intuition is pretty straightforward. As the given arrays are sorted, we are using 2 pointer approach to get a third array, that contains all the elements from the given two arrays in the sorted order. Now, from the sorted third array, we are again filling back the given two arrays.



def merge(arr1, arr2, n, m):

    # Declare a 3rd array and 2 pointers:
    arr3 = [0] * (n + m)
    left = 0
    right = 0
    index = 0

    # Insert the elements from the 2 arrays
    # into the 3rd array using left and right
    # pointers:
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1

    # If right pointer reaches the end:
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1

    # If left pointer reaches the end:
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1

    # Fill back the elements from arr3[]
    # to arr1[] and arr2[]:
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print() 

# Time Complexity: O(n+m) + O(n+m), where n and m are the sizes of the given arrays.
# Reason: O(n+m) is for copying the elements from arr1[] and arr2[] to arr3[]. And another O(n+m) is for filling back the two given arrays from arr3[].