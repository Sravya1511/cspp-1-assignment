"""square"""
def square(x_x):
    """sq"""
    c_c = x_x*x_x
    return c_c
def main():
    """sq"""
    data_ = input()
    data_ = float(data_)
    temp_ = str(data_).split('.')
    if temp_[1] == '0':
        print(square(int(float(str(data_)))))
    else:
        print(square(data_))
if __name__ == "__main__":
    main()
