#Intuition: We can simply use 2 loops and track every transaction and maintain a variable maxPro to contain 
# the max value among all transactions.


from typing import List

def maxProfit(arr: List[int]) -> int:
    maxPro = 0
    n = len(arr)


    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                maxPro = max(arr[j] - arr[i], maxPro)


    return maxPro


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    maxPro = maxProfit(arr)
    print("Max profit is: ", maxPro)

# Time complexity: O(n^2)

# Space Complexity: O(1)
