#so its called expand around center
'''
    Time Complexity : O(N ^ 2)
    Space Complexity: O(1)
    
    Where N is the length of the string.
'''

def expandAroundCenter(str: str, left: int, right: int) -> int:

    start = left
    end = right
    
    n = len(str)

    # Expand the center.
    while (start >= 0 and end < n and str[start] == str[end]):
        start -= 1
        end += 1

    return end - start - 1


def longestPalinSubstring(str: str) -> str:
    n= len(str)

    if n < 1:
        return ""

    start = 0
    end = 0
    for i in range(n):

        # Longest odd length palindrome with center points as i.
        len1 = expandAroundCenter(str, i, i)

        # Longest even length palindrome with center points as i and i + 1.
        len2 = expandAroundCenter(str, i, i+1)

        length = max(len1, len2)


        #here start and end are the indexes of the longest palindromic substring



        #here the condition means that if the length of the current palindromic substring is greater than
        #the previous one then update the start and end indexes

        #but dont we do it in length = max(len1, len2) ??
        #i mean we are already checking the length of the current palindromic substring
        #then why do we need to check it again ??
        #because we are checking the length of the current palindromic substring
        #but we are not checking the length of the longest palindromic substring
        #so we need to check it again


        
        if (length > end - start + 1):
            start = i - (length - 1) // 2
            end = i + (length) // 2

    return str[start : end + 1]

print(longestPalinSubstring("babad"))