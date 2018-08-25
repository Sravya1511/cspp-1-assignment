'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    """string"""
    s_t = string.split('\n')
    dic = {}
    li_1 = []

    for i in range(len(s_t) -1):
        data = s_t[i].split(" ")
        # print(data)
        li_1.extend(data)
        
    for i in word:
        if i in '"' ',' ';':
            word = word.replace(i, "")
        dic[word] = li_1.count(word)
    return dic

def main():
    """main"""
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
