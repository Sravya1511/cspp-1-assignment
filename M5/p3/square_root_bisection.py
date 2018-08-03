# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
x_1 = int(input())
epsilon_1 = 0.01
low_1 = 0.0
high_1 = x_1
ans_1 = (high_1 + low_1)/2.0
while abs(ans_1**2 - x_1) >= epsilon_1:
    if ans_1**2 < x_1:
        low_1 = ans_1
    else:
        high_1 = ans_1
    ans_1 = (high_1 + low_1)/2.0
print(str(ans_1))