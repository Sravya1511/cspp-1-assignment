'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    list1 = data.split (' ')
    key = []
    value = []
    list2 = []
    dictionary_ = {}
    x = 1
    j = 0
    # return list1
    # for i in range(len(list1)):
    for i in range(len(list1)):
        if list1[i] == "follows":
            key.append(list1[i-1])
            # value.append(list1[j+1])
    # for i in range(len(list1)-1):
    for i in range(len(list1)):
        if list1[i] == "follows":
            j = i+1
            value.append(list1[j])
        #     print(j)
        #     while list1[j] != key[x]:
        #         value.append(list1[j+1])
        #         j = j+1
        #     x = x+1
        # i = j
    dictionary_ = dict(zip(key, value))
                # if i == len(list1)
                # i = i+1
    return dictionary_

                
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    import string


def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
