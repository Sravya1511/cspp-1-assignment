# Write a python program to find the square root of the given number 
# using approximation method
def main():
	S_1 = int(input())
	epsilon_1 = 0.01
	guess_1 = 0
	incre_1 = 0.001
	while(abs(guess_1**2 - S_1) >= epsilon_1 and guess_1 <= S_1):
		guess_1 += incre_1
	if abs(guess_1**2 - S_1 >= epsilon_1):
		print("No square")
	else:
		print("sqaure" + str(guess_1))
if __name__== "__main__":
	main()