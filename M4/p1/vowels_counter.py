#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    string_1 = input()
    count_1 = 0
    for letter in string_1:
        if letter in 'a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U':
            count_1 = count_1+1
    print(count_1)

if __name__== "__main__":
	main()
