class Solution:
    def partition(self, s: str):
        
        def isPalindrome(start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        ans = []

        def recur(ind, sub):
            print(sub)
            if ind == len(s):
                ans.append(sub)
                return
            
            for i in range(ind, len(s)):

                if isPalindrome(ind, i):  # Corrected the indices

                    print("i=",end=" ")
                    print(i,end=" ")
                    print("ind=",end=" ")
                    print(ind,end=" ")
                    print("sub=",end=" ")
                    print(sub,end=" ")
                    print("s[ind:i+1]=",end=" ")
                    print(s[ind:i+1],end=" ")
                    recur(i + 1, sub + [s[ind:i+1]])  # Corrected slicing and appending as a list

        recur(0, [])  # Corrected to pass an empty list for `sub`
        return ans
    
s=Solution()
print(s.partition("aab"))