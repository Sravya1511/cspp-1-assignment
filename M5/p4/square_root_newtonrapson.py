"""Write a python program to find the square root of the given number"""
def main():
    """nr"""
    step_ = 0.01
    y_q = int(input())
    guess_ = y_q/2.0
    nog_ = 0
    while abs(guess_*guess_ - y_q) >= step_:
        nog_ += 1
        guess_ = guess_ - (((guess_**2) - y_q)/(2*guess_))
    print(str(guess_))
if __name__ == "__main__":
    main()
