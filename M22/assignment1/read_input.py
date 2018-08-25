'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines = int(input())
    string = ""
    for i in range(lines):
    	string = string + input()
    	string = string + '\n'
    print(string)

if __name__ == '__main__':
    main()
