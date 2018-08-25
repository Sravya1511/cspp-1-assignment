'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
	li = []
	li.append(dictionary.keys())
    li.sort()
    # print(sortedkeys)
    for i in li:
    	print(i, "-", dictionary[i])
   

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
