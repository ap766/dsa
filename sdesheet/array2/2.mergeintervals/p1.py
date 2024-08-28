# The intuition of this approach is pretty straightforward. We are just grouping close
#  intervals by sorting the given array. After that, we merge an interval 
# with the other by checking if one can be a part of the other interval. 
# For this checking, we are first selecting a particular interval using a 
# loop and then we are comparing the rest of the intervals using another loop.


# Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.
# Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j. But while using loop i, we skip all the intervals that are merged with loop j. So, we can conclude that every interval is roughly visited twice(roughly, once for checking or skipping and once for merging). So, the time complexity will be 2*N instead of N2.
#BASICALLY THE LOOP INSIDE IS VISITED 2 TIMES ONLY INSTEAD OF N TIMES.


from typing import List

def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = arr[i][0], arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans

if __name__ == '__main__':
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = mergeOverlappingIntervals(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()




