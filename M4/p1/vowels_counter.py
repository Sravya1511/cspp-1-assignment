#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    String_1 = input()
    Count_1 = 0
    for letter in String_1:
        if letter in 'a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U':
            Count_1 = Count_1+1
    print(Count_1)

if __name__== "__main__":
	main()
