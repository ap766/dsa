#Here the time complexity i have a doubt is it O(n^3) or O(n^2) ?
#And also if space if n2 or n ?


L=[]
def printSubStrings(str):
    # First loop for starting index
    for i in range(len(str)):
        subStr = ""

        # Second loop is generating sub-String
        for j in range(i, len(str)):
            subStr += str[j]
            L.append(subStr)

    return sorted(L, key=len, reverse=True)

def isPalindrom(sub):
    n = len(sub)
    i = 0
    j = n - 1
    while i < j:
        
        if(sub[i] != sub[j]):
            return False
        
        i += 1
        j -= 1

    return True

def longestPalinSubstring(str):

    K=printSubStrings(str)

    for i in K:
        if (isPalindrom(i)):
            return i
        
    return ""
