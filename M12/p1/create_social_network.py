"""Assignment-1 Create Social Network"""
def create_social_network(data):
    """split"""
    new_data = data.split('\n')
    dic_1 = {}
    # print(data)
    for i in range(len(new_data)-1):
        data_1 = new_data[i].split(" follows ")
        print(data_1)
        if len(data_1) <= 1:
            return dic_1
        elif new_data[i] in dic_1:
            dic_1[i][0].append(dic_1[i][1].split(','))
        else:
            dic_1[i][0] = dic_1[i][1].split(',')
    return dic_1
        

                # i = i+1
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
