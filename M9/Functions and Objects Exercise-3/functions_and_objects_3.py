#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
def square(x):
    x = x*x
    return x

def apply_to_each(L, square):
    le = len(L)
    L1 = ()
    for i in range(0, le):
        L[i] = square(L[i])
        L1 = L1 + (L[i],)
    return L1 
    
def main():
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))
if __name__== "__main__":
	main()