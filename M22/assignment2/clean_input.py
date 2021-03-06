'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''


def clean_string(string):
    """clean string"""

    for i in string:
        if i in '!' '@' '#' '$' '%' '^' '&' '*' ' ' '.' '(' ')':
            string = string.replace(i, "")
    # if len(string) == 0:
    #     return " "
    return string

def main():
    """main"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
