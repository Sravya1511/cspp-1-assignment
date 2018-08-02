#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    S = input()
    C = 0
    for letter in S:
        if letter in 'a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U':
            C = C+1
    print("Number of vowels:"+ str(C))

if __name__== "__main__":
	main()
