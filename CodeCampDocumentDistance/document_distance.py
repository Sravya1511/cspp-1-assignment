'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re

def similarity(dict1, dict2):
    """similarity"""
    # dic = {}
    # str1 = str(dict1)
    # str2 = str(dict2)
    # str1.strip()
    # str2.strip()
    # list1 = str1.lower().split()
    # list2 = str2.lower().split()

    # stopwords = load_stopwords("stopwords.txt")
    # for i in list1:
    #     if i in stopwords:
    #         list1.remove(i)
    # # print(list1)
    # for i in list2:
    #     if i in stopwords:
    #         list2.remove(i)

    # # print(list2)
    # # print(list1)
    # # print(list2)
    # list3 = list1 + list2
    # # print(list3)
    # # for i in list1:
    # #     if i not in dic:
    # #         dic[i] = [list1.count(i)]
    # # print(dic)
    # # for i in list2:
    # #     if i in dic:

    # #         dic[i].append(str(list2.count(i)))
    # #     if i not in dic:
    # #         dic[i] = [list2.count(i)]
    # # print(dic)
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
    regex = re.compile('[^a-z]')
    words1 = [regex.sub("", w.strip()) for w in dict1.lower().split(" ")]
    words2 = [regex.sub("", w.strip()) for w in dict2.lower().split(" ")]

    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for w_1 in words1:
        if w_1 not in stopwords and len(w_1) > 0:
            if w_1 not in dictionary.keys():
                dictionary[w_1] = [0, 0]
            dictionary[w_1][0] += 1


    for w_1 in words2:
        if w_1 not in stopwords and len(w_1) > 0:
            if w_1 not in dictionary.keys():
                dictionary[w_1] = [0, 0]
            dictionary[w_1][1] += 1

    num = sum([v1*v2 for v1, v2 in dictionary.values()])
    den1 = math.sqrt((sum([v1**2 for v1, v2 in dictionary.values()])))
    den2 = math.sqrt((sum([v2**2 for v1, v2 in dictionary.values()])))

    return num/(den1*den2)
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
