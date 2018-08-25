'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    sortedkeys = sorted(dictionary, key=str)
    for i in sortedkeys:
        print(i, "-", graph(i, dictionary))

def graph(i, dictionary):
    for i in dictionary:
        s = ''
        count = 0
        for j in dictionary[i]:
            while count < j:
                s = s+"#"
                count += 1
        return s
            

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
