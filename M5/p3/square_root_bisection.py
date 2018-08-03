"""bisect"""
def main():
    """bisection"""
    x_q = int(input())
    epsilon_ = 0.01
    numuesses_ = 0
    low_ = 0.0
    high_ = x_q
    ans_ = (high_ + low_)/2.0
    while abs(ans_**2 - x_q) >= epsilon_:
        numuesses_ += 1
        if ans_**2 < x_q:
            low_ = ans_
        else:
            high_ = ans_
        ans_ = (high_ + low_)/2.0
    print(str(ans_))
if __name__ == "__main__":
    main()
