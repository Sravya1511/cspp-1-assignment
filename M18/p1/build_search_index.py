'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    # str1 = str(text)
    # list1 = str1.lower().split(" ")
    # stopwords = load_stopwords("stopwords.txt")
    # for i in list1:
    #     if i in stopwords:
    #         list1.remove(i)
    # print(list1)
    # regex = re.compile('[^a-z]')
    # words1 = [regex.sub(" ", w.strip()) for w in list1]
    # print(words1)

    # return words1
    # regex = re.compile('[^a-z]')
    # words1 = [regex.sub("", w.strip()) for w in str1.lower().split(" ")]
    # # stopwords = load_stopwords("stopwords.txt")
    # # for i in words1:
    # #     if i in stopwords:
    # #         words1.remove(i)
    # return words1

    text = str(text)
    regex = re.compile('[^a-z]')
    wordlist1 = [regex.sub("", w.strip()) for w in text.lower().split(" ")]
    # print(word_list)
    return wordlist1



def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    # stopwords = load_stopwords("stopwords.txt")
    # list_1 = docs
    # # for i in list_1:
    # #     if i in stopwords:
    # #         list_1.remove(i)
    # dic = {}
    # list_2 = word_list(docs)
    # # print(list_1)
    # # print(list_2)
    # for i in list_2:
    # 	# if i not in stopwords:
    #     # if i not in dic:
    #         for j in range(len(list_1)):
    #             str1 = list_1[j]
    #             list_temp = str1.split(" ")
    #             if i in list_temp:
    #                 if i not in dic:
    #                     dic[i] = [(j, list_temp.count(i))]
    #                 else:
    #                     dic[i].append((j, list_temp.count(i)))
    # return dic
    # # b = word_list(docs)
    # # print(b)

    search_index = {}
    stopwords = load_stopwords('stopwords.txt')
    # l1 = word_list(docs)
    def remove(stopwords, wordslist):
        l2_ = []
        for i in wordslist:
            if i not in stopwords:
                l2_.append(i)
        return l2_
    for index, doc in enumerate(docs):
        list_1 = word_list(doc)
        list_1 = remove(stopwords, list_1)
        for word in set(list_1):
            if word in search_index:
                search_index[word].append((index, list_1.count(word)))
            else:
                search_index[word] = [(index, list_1.count(word))]
    return search_index



# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
