"""factorial"""
def factorial_1(n_1):
    """fact"""
    if n_1 == 1 or n_1 == 0:
        return 1
    return n_1*factorial_1(n_1-1)
def main():
    """fact"""
    a_1 = input()
    print(factorial_1(int(a_1)))
if __name__ == "__main__":
    main()
