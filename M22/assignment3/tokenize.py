'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    s = string.split('\n')
    dic = {}
    li = []

    for i in range(len(s) -1):
        data = s[i].split(" ")
        print(data)
        li.extend(data)
    print(li)



        
       


    
            
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
