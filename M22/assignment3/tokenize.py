'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    s = string.split('\n')
    dic = {}
    for i in s:
        word = i.split(" ")
        print(word)
        
       


    
            
def main():
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
