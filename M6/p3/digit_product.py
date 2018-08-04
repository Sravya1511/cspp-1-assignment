'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    """product"""
    int_input = int(input())
    N = abs(int_input)
    P = 1
    R = 0
    while N >= 1:
        R = N%10
        P = P*R
        N = N//10
    if int_input < 0:
        P = -P
    print(P)
if __name__ == "__main__":
    main()
