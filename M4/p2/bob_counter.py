"""bob counter"""
def main():
    """bob"""
    s_a = input("Enter a string ")
    s_b = 'bob'
    a_1 = len(s_a)
    co_ = 0
    for i in range(a_1-2):
        if s_b == s_a[i]+s_a[i+1]+s_a[i+2]:
            co_ = co_+1
    print(co_)
if __name__ == "__main__":
    main()
