"""Exercise: Assignment-4"""
def calculateHandlen(hand):
    """sum"""
    sum_1 = 0
    for i_1 in hand:
        sum_1 = sum_1 + hand[i_1]
    return sum_1
def main():
    """sum"""
    n_1 = input()
    adict = {}
    for i_1 in range(int(n)):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    print(calculateHandlen(adict))
if __name__ == "__main__":
    main()
