#This would have O(n^3) time complexity
#This would have O(1) space complexity
#But issue is it using slice function


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

def generate_substrings_descending_order(input_str):
    n = len(input_str)

    for length in range(n, 0, -1):
        for j in range(n - length + 1):
       
           if isPalindrom(input_str[j:j + length]):
               return input_str[j:j + length]

print(generate_substrings_descending_order("babad"))