def check(pat, z):
    for i in range(len(z)):
        # If the size of the pattern string is equal to the ith index of the z array
        if z[i] == len(pat):
            return True
    return False

def createZArray(concatenated, z):
    left = right = 0
    for i in range(1, len(concatenated)):
        if i > right:
            left = right = i
            while right < len(concatenated) and concatenated[right] == concatenated[right - left]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < len(concatenated) and concatenated[right] == concatenated[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1

def main():
    # Taking pattern and text string as input
    text = input()
    pat = input()

    # Creating array to store values of Z array
    z = [0] * (len(text) + len(pat) + 1)
    concatenated = pat + "#" + text

    # Function call
    createZArray(concatenated, z)
    if check(pat, z):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
