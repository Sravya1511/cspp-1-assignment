"""iteration"""
def iter_power(base_, exp_):
    P_1 =1
    for i in range(1, exp_+1):
        P_1 = base_*P_1
    return P_1
def main():
    """iteration"""
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1]))) 
if __name__ == "__main__":
    main()
