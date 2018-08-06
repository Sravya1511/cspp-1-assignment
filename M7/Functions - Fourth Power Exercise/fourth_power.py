"""fourth"""
def square_1(x_1):
    """square"""
    c_1 = x_1*x_1
    return c_1
def fourth_power(x_1):
    """square"""
    y_1 = square_1(square_1(x_1))
    return y_1
def main():
    """square"""
    data_1 = input()
    data_1 = float(data_1)
    temp_1 = str(data_1).split('.')
    if temp_1[1] == '0':
        print(fourth_power(int(float(str(data_1)))))
    else:
        print(fourth_power(data_1))
if __name__ == "__main__":
    main()
