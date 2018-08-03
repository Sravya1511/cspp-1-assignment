"""Write a python program to find if the given number is a perfect cube or not. using guess and check algorithm"""
def main():
    """guess"""
    r_1 = int(input())
    s_1 = abs(r_1)
    for guess_1 in range(1, s_1+1):
        if guess_1**3 >= s_1:
            break
    if guess_1**3 != s_1:
        print(str(r_1) + " is not a perfect cube")
    elif guess_1**3 == s_1:
        if r_1 < 0:
            guess_1 = -guess_1
        print(str(r_1) + " is a perfect cube")  
            if __name__ == "__main__":
    main()
