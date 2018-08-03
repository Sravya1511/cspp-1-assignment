""" Write a python program to find the square root of the given number """
def main():
    """square"""
    x_1 = int(input())
    epsilon_ = 0.01
    cla_ = 0
    guess_ = 0.0
    increment_ = 0.0001
    num_guesses = 0
    while abs(guess_**2 - x_1) >= epsilon_:
        guess_ += increment_
        num_guesses += 1
    if abs(guess_**2 - x_1) >= epsilon_:
        cla_ = cla_ + 1
    else:
        print(str(guess_))
if __name__ == "__main__":
    main()
