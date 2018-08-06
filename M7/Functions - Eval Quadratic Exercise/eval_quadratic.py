"""qua"""
def eval_quadratic(a_1, b_1, c_1, x_1):
    """quadratic"""
    s_1 = a_1*x_1*x_1 + b_1*x_1 + c_1
    return s_1
def main():
    """qua"""
    data_1 = input()
    data_1 = data_1.split(' ')
    data_1 = list(map(float, data_1))
    y_1 = len(data_1)
    for x_1 in range(y_1):
        temp_1 = str(data_1[x_1]).split('.')
        if temp_1[1] == '0':
            data_1[x_1] = int(float(str(data_1[x_1])))
        else:
            data_1[x_1] = data_1[x_1]
    print(eval_quadratic(data_1[0], data_1[1], data_1[2], data_1[3]))
if __name__ == "__main__":
    main()
