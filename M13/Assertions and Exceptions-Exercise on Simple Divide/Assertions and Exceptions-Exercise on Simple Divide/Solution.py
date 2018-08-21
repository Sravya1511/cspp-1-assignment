#define the simple_divide function here
# def simple_divide(item, denom):
#     li = []
#     for i in range(len(item)):
#         li.append(item[i]/float(denom))
#     return li
    
   
def fancy_divide(list_of_numbers, index):
    li = []
    denom = list_of_numbers[index]
    for i in range(len(list_of_numbers)):
        try:
            li.append(list_of_numbers[i]/float(denom))
            # print("no ERRor")
        except ZeroDivisionError:
            # simple_divide(list_of_numbers, denom)
            # print("error found")
            li.append(0)
            # print("error")
    return li

def main():
    data = int(input())
    # l=data.split()
    l1=[]
    for i in range(data):
        j = float(input())
        l1.append(float(j))
    s=input()
    index=int(s)
    # l1 = [9, 3, 12]
    # index = 1
    print(fancy_divide(l1, index))

if __name__== "__main__":
    main()
