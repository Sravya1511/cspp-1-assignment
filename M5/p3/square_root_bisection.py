"""bisect"""
def main():
    """bisection"""
    x_ = int(input())
    epsilon_ = 0.01
    numGuesses_ = 0
    low_ = 0.0
    high_ = x_
    ans_ = (high_ + low_)/2.0
    while abs(ans_**2 - x_) >= epsilon_:
        numGuesses_ += 1
        if ans_**2 < x_:
            low_ = ans_
        else:
            high_ = ans_
        ans_ = (high_ + low_)/2.0
    print(str(ans_))
if __name__ == "__main__":
    main()
