# '''
#     Time complexity: O(n + m)
#     Space complexity: O(1)

#     Where 'n' and 'm' are the lengths of 'text' and 'pattern' respectively.
# '''
# from typing import List

# def modPower(a: int, b: int, mod: int) -> int:
#     if b == 0:
#         return 1

#     p = modPower(a, b // 2, mod)
#     if b % 2 == 1:
#         return (p * p * a) % mod
#     return (p * p) % mod

# def stringMatch(text : str, pattern: str) -> List[int]:
#     n = len(text)
#     m = len(pattern)

#     # List storing the indices of occurrences.
#     ans = []

#     MOD = 1000000007

#     maxPow = modPower(26, m - 1, MOD)

#     print(maxPow)

#     hashPattern = 0
#     hashText = 0
#     for i in range(m):
#         hashPattern = (hashPattern * 26 + ord(pattern[i]) - ord('a')) % MOD
#         print(hashPattern)

#     print("gap")

#     for i in range(m - 1):
#         hashText = (hashText * 26 + ord(text[i]) - ord('a')) % MOD
#         print(hashText)
#     print("k")
    
#     for i in range(n - m + 1):
#         # Adding the last character in hash.
#         hashText = (hashText * 26 + ord(text[i + m - 1]) - ord('a')) % MOD

#         print(hashText)

#         if hashText == hashPattern:
#             # Checking if the substring is equal to 'pattern'.
#             match = True

#             for j in range(m):
#                 # If a character mismatch occurs.
#                 if text[i + j] != pattern[j]:
#                     match = False
#                     break

#             if match:
#                 ans.append(i + 1)

#         # Removing the first character in hash.
#         hashText = (hashText - maxPow * (ord(text[i]) - ord('a'))) % MOD
#         hashText = (hashText + MOD) % MOD

#     return ans

# print(stringMatch("codes","code"))

#The leetcode question but tc is a lot
from typing import List

class Solution:
    PRIME = 101
    S = 10

    @staticmethod
    def calc_hash(string):
        hash_value = 0
        for i in range(len(string)):
            hash_value += (ord(string[i]) - ord('a') + 1) * pow(Solution.S, len(string) - i - 1)       
        hash_value %= Solution.PRIME  
        return hash_value

    @staticmethod
    def recalc_hash(old_hash, old_char, new_char, pattern_length):
        sub = (ord(old_char) - ord('a') + 1) * pow(Solution.S, pattern_length - 1)
        hash_value = old_hash - sub
        hash_value *= Solution.S
        hash_value += (ord(new_char) - ord('a') + 1)
        hash_value %= Solution.PRIME 
        return hash_value

    @staticmethod
    def search(text, pattern):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_hash = Solution.calc_hash(pattern)
        text_hash = Solution.calc_hash(text[:pattern_length])

        for i in range(text_length - pattern_length + 1):
            if text_hash == pattern_hash:
                if text[i:i + pattern_length] == pattern:
                    return True

            if i < text_length - pattern_length:
                text_hash = Solution.recalc_hash(text_hash, text[i], text[i + pattern_length], pattern_length)

        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b or b in a:
            return 1  
        
        count = 1
        source = a
        
        while len(source) < len(b) + len(a):
            count += 1
            source += a
            if self.search(source, b): 
               return count

        return -1  
    
#The coding ninjas question

from typing import List
class Solution:
    PRIME = 101
    S = 10

    @staticmethod
    def calc_hash(string):
        hash_value = 0
        for i in range(len(string)):
            hash_value += (ord(string[i]) - ord('a') + 1) * pow(Solution.S, len(string) - i - 1)
        hash_value %= Solution.PRIME  # Apply modulo operation after the entire calculation
        return hash_value

    @staticmethod
    def recalc_hash(old_hash, old_char, new_char, pattern_length):
        old_char_hash = (ord(old_char) - ord('a') + 1) * pow(Solution.S, pattern_length - 1)
        hash_value = old_hash - old_char_hash
        hash_value *= Solution.S #Since we lost one 10
        hash_value += (ord(new_char) - ord('a') + 1) #Since Last one is Anyways 10**0
        hash_value %= Solution.PRIME  # Apply modulo operation after the entire calculation
        return hash_value

    @staticmethod
    def search(text, pattern):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_hash = Solution.calc_hash(pattern)
        text_hash = Solution.calc_hash(text[:pattern_length])
        match_indices = []

        for i in range(text_length - pattern_length + 1):
            if text_hash == pattern_hash:
                if text[i:i + pattern_length] == pattern:
                    match_indices.append(i+1)

            if i < text_length - pattern_length:
                text_hash = Solution.recalc_hash(text_hash, text[i], text[i + pattern_length], pattern_length)

        return match_indices

def stringMatch(text: str, pattern: str) -> List[int]:
    match_indices = Solution.search(text, pattern)
    return match_indices
