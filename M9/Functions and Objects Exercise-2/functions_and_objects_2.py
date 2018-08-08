#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def f(x):
    x = x+1
    return x
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
    print(apply_to_each(list1, f))
if __name__ == "__main__":
    main()
