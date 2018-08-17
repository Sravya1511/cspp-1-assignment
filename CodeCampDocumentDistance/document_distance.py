'''
    Document Distance - A detailed description is given in the PDF
'''
import math

def similarity(dict1, dict2):
    dic = {}
    str1 = str(dict1)
    str2 = str(dict2)
    str1.strip()
    str2.strip()
    list1 = str1.lower().split()
    list2 = str2.lower().split()
   
    

    stopwords = load_stopwords("stopwords.txt")
    for i in list1:
        if i in stopwords:
            list1.remove(i)
    # print(list1)
    for i in list2:
        if i in stopwords:
            list2.remove(i)
    # print(list2)
    # print(list1)
    # print(list2)
    # list3 = list1 + list2
    # print(list3)
    for i in list1:
        if i not in dic:
            dic[i] = [list1.count(i)]
    print(dic)
    for i in list2:
        if i in dic:
            dic[i].append(str(list2.count(i)))
        if i not in dic:
            dic[i] = [list2.count(i)]
    print(dic)
    # for i in list3:
    #     if i not in dic:
    #         dic[i] = [list1.count(i), list2.count(i)]
    # # print(dic)
    # numerator = 0.0
    # for i in dic:
    #     a = dic[i][0]
    #     b = dic[i][1]
    #     numerator = numerator + a*b
    # # print(numerator)
    # s1 = 0.0
    # s2 = 0.0
    # for i in dic:
    #     s1 = s1 + (dic[i][0]**2)
    #     s2 = s2 + (dic[i][1]**2)
    # sq1 = math.sqrt(s1)
    # sq2 = math.sqrt(s2)
    # denominator = sq1*sq2
    # res = numerator//denominator
    # return res



    '''
        Compute the document distance as given in the PDF
    '''
    

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
