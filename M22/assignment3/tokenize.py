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
        # print(data)
        li.extend(data)
    for word in li:
        for i in word:
            if i in '"':
                word = word.replace(i, "")
        dic[word] = li.count(word)
    return dic
    
            
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
