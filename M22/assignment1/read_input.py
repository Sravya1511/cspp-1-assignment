'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """read string"""
    lines = int(input())
    string = ""
    for i in range(lines):
        string = string + input()
        i = i+1
        string = string + '\n'
    print(string)

if __name__ == '__main__':
    main()
