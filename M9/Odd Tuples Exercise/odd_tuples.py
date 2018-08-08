"""tuple"""
def oddTuples(aTup):
    """tuple"""
    odd = ()
    l = len(aTup)
    j= 0
    while j < l:
        odd = odd + (aTup[j],)
        j = j+2
    return odd
def main():
    """tuple"""
    data = input()
    data = data.split()
    aTup = ()
    for j in range(len(data)):
        aTup += (int(data[j]),)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()
    --