'''
    Time Complexity     :   O(N)
    Space Complexity    :   O(N)

    Where 'N' is the length of the string.
    
'''
def romanToIntHelper(s: str, conv: dict) -> int:

    # If single charecter, then return the integer value of that charcter.
    if(len(s) <= 1):
        return conv[s]

    # Take first 2 charecters.
    firstTwo = s[0:2]
    print(firstTwo)

    # If the first 2 charecters are in the dict 'conv' , add their value and check rest of the string.
    if(firstTwo in conv):
        print("k",end=" ")
        print(firstTwo)
        return conv[firstTwo]+romanToIntHelper(s[2:], conv)

    # Otherwise take one charecter and check its value.
    else:
        print("B",end=" ")
        print(firstTwo)
        firstOne = s[0]
        return conv[firstOne]+romanToIntHelper(s[1:], conv)


def romanToInt(s: str) -> int:
    conv = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "": 0}
    return romanToIntHelper(s, conv)

print(romanToInt("MCMXCIV"))