'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''
def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    # remove the pass below and start writing your code
    # l_1 = []
    # for i in network:
    #     if i == arg1:
    #         l_1 = network[i]
    #         l_1.append(arg2)
    #         network[i] = l_1
    # return network
    if arg1 in network:
        network[arg1].append(arg2)
    else:
        network[arg1] = [arg2]
    return network
def unfollow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    # remove the pass below and start writing your code
    network[arg1].remove(arg2)
    return network
def delete_person(network, arg1):
    """delete"""
    dict_1 = network
    if arg1 in dict_1:
        del dict_1[arg1]
    dict_2 = dict_1
    x_1 = []
    # x = []
    # # for i in range(len(dict_1)):
    # # #     for j in range(len(dict_1[i])):
    # # #         if arg1 == dict_1[i[j]]:
    # # #             del dict_1[i[j]]
    # # # return dict_1
    # # if in dict_1.values():
    # #     del dict_1.values[arg1]
    # for i in dict_2:
    #     # x = dict_2[i]
    #     if arg1 in dict_2[i]:
    #         dict_2[i].remove('arg1')
    #     # dict_2[i] = x
    for i in dict_2:
        # print(dict_2[i])
        x_1 = dict_2[i]
        if arg1 in x_1:
            x_1.remove(arg1)
        dict_2[i] = x_1


    return dict_2

def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])

    print(network)
if __name__ == "__main__":
    main()
