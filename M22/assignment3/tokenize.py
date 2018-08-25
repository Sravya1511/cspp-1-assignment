'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    """string"""
    s_t = string.split('\n')
    dic = {}
    li_1 = []
    li_new = []

    for i in range(len(s_t) -1):
        data = s_t[i].split(" ")
        for i in data:
            if i in '"' ',' ';':
                word = word.replace(i, "")
        # print(data)
        li_1.extend(data)
        for i in li_1:
            if i in '"' ',' ';':
                word = word.replace(i, "")
            li_new.extend(word)
    for word in li_new:
        # for i in word:
        #     if i in '"' ',' ';':
        #         word = word.replace(i, "")
        dic[word] = li_new.count(word)
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
