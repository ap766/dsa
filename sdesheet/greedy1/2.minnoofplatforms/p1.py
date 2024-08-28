#1.Max number of intersections if we notice
#2.If intersecting we need more platforms
#3. 4 Cases . Either Arrive previously and depart later .
#. Arrive later and depart earlier
#. Arrive later and depart later
#. In between


def countPlatforms(n, arr, dep):
    ans = 1  # final value
    for i in range(n):
        count = 1  # count of overlapping interval of only this iteration
        for j in range(i+1, n):
            #first cond =This checks if train i arrives during the time train j is at the platform.
            #second cond =This checks if train j arrives during the time train i is at the platform.
            if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
                count += 1

        ans = max(ans, count)  # updating the value
    return ans




if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    n = len(dep)
    print("Minimum number of Platforms required", countPlatforms(n, arr, dep))