def longestSubarrayWithSumK(a, k: int) -> int:
       
        n=len(a)
        left, right = 0, 0  # 2 pointers
        Sum = 0  # Start with 0 sum
        maxLen = 0

        while right < n:  # Continue until right pointer reaches the end of the array
            Sum += a[right]  # Add the current element to the sum

            while Sum > k:  # Shrink the window if the sum exceeds k
                Sum -= a[left]
                left += 1

            if Sum == k:  # Check if the current sum equals k
                maxLen = max(maxLen, right - left + 1)

            right += 1  # Move the right pointer forward

        return maxLen


#here the while loop ting is that if u use if u could miss out on some potential answers