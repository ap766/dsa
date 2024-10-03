class Solution:
    def reverse(self,arr, start, end):
                while start <= end:
                    temp = arr[start]
                    arr[start] = arr[end]
                    arr[end] = temp
                    start += 1
                    end -= 1
    def rotate(self, arr, k: int) -> None:
    
            # Handle cases where k > n
            n=len(arr)
            k = k % n
            # Reverse the first n-k elements
            self.reverse(arr, 0, n - k - 1)
            # Reverse the last k elements
            self.reverse(arr, n - k, n - 1)
            # Reverse the whole array
            self.reverse(arr, 0, n - 1)
            
          

            