# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    x_1 = int(input())
    approx_1 = 0.01
    low_1 = 0
    high_1 = x_1
    guess_1 = (low_1 + high_11)//2
    while guess_1**2 - x_1 >= approx_1:
        if guess_1**2 < x_1:
            low_1 = guess_1
        if guess_1**2 > x_1:
            high_1 = guess_1
    guess_1 = (low_1 + high_1)//2
    print(str(guess_1))    
if __name__== "__main__":
	main()
