#BASICALLY JUST LIKE INVERSE BUT 2 DIFFERENCES - THAT WE ADD FOR ENTIRE IN THAT AND WE ADD FOR EACH HERE
#AND THERE HAS TO BE A SEPERATE FUNCTION
#AND TC IS N+N CUS WE DONT GO THRU WHOLE ARRAY FOR POINTER IN FIRST ARRAY , WE GO THRU SECTIONS OF SECOND ARRAY

#extra point - please ask interviewer if u should create a copy.

from typing import List

def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def team(skill, n: int) -> int:
    return mergeSort(skill, 0, n - 1)

if __name__ == "__main__":
    a = [4, 1, 2, 3, 1]
    n = 5
    cnt = team(a, n)
    print("The number of reverse pair is:", cnt)


