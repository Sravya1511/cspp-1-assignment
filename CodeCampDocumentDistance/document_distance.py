'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    
    str1 = str(dict1)
    str2 = str(dict2)
    list1 = str1.lower().split()
    list2 = str2.lower().split()
    # print(list1)
    # print(list2)
    list1.strip()
    list2.strip()
    print(list1)
    print(list2)

    stopwords = load_stopwords("stopwords.txt")
    for i in list1:
        if i in stopwords:
            list1.remove(i)
    print(list1)
    for i in list2:
        if i in stopwords:
            list2.remove(i)
    print(list2)

    '''
        Compute the document distance as given in the PDF
    '''
    pass

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
