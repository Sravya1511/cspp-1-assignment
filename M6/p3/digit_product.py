'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    """product"""
    int_input = int(input())
    n_1 = abs(int_input)
    p_1 = 1
    r_1 = 0
    if n_1 == 0:
    	print(n_1)
    else:
        while n_1 >= 1:
            r_1 = n_1%10
            p_1 = p_1*r_1
            n_1 = n_1//10
        if int_input < 0:
            p_1 = -p_1
        print(p_1)
if __name__ == "__main__":
    main()
