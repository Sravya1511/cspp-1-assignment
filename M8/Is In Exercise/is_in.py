# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    low = 0
    high = len(aStr)
    mid = (low+high)//2
    if low == high:
        if char == aStr:
            return True
    if high == 0:
        return False
    while (low!=high):
        if aStr[mid] == char:
            return True
        else:
            if aStr[mid] > char:
                return value(low, mid)
            elif aStr[mid] > char:
                return value(mid, high)
    return 0
def value(low, high): 
    mid = (low+high)//2
    if aStr[mid] == char:
        return True
    return 0


def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()