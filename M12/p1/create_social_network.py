"""Assignment-1 Create Social Network"""
def create_social_network(data):
    """split"""
    new_data = data.split('\n')
    dic_1 = {}
    # print(data)
    for i in range(len(new_data)-1):
        data_1 = new_data[i].split(" follows ")
        # print(data_1)
        if len(data_1) <= 1:
            return dic_1
        if data_1[0] in dic_1:
            dic_1[data_1[0]].append(data_1[1].split(','))
        else:
            dic_1[data_1[0]] = data_1[1].split(',')
    return dic_1


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
