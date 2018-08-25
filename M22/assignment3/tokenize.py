'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
	s = string.split('\n')
	print(s)

    
            
def main():
	lines = int(input())
    string = ""
    for i in range(lines):
        string = string + input()
        i = i+1
        string = string + '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
