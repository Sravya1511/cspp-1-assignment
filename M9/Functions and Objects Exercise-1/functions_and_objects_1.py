def apply_to_each(L, f):
    le = len(L)
    L1 = ()
    for i in range(0, le):
        L[i] = f(L[i])
        L1 = L1 + (L[i],)
    return L1
def main():
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    var = apply_to_each(list1, abs)
    print(var)
if __name__ == "__main__":
    main()
