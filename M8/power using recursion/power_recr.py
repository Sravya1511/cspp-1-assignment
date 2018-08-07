"""recurssion"""
def recur_power(base_, exp_1):
    """recursion"""
    if exp_1 == 1:
        return base_
    else:
        return base_*recur_power(base_, exp_1-1)
def main():
    """recursion"""
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
