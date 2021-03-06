'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """freq"""
    sortedkeys = sorted(dictionary, key=str)
    for i in sortedkeys:
        print(i, "-", graph(i, dictionary))

def graph(i, dictionary):
    """sorted"""
    s_1 = ''
    count = 0
    while count < dictionary[i]:
        s_1 = s_1+"#"
        count += 1
    return s_1


def main():
    """main"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
