"""Write a python program to find the square root of the given number"""
def main():
    """nr"""
	step_ = 0.01
    y_ = int(input())
    guess_ = y_/2.0
    nog_ = 0
    while abs(guess_*guess_ - y_) >= step_:
        nog_ += 1
        guess_ = guess_ - (((guess_**2) - Y_)/(2*guess_))
    print('numGuesses = ' + str(nog_))
    print('Square root of ' + str(y_) + ' is about ' + str(guess_))
if __name__== "__main__":
    main()
