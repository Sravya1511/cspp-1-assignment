'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''
def get_available_letters(letters_guessed):
    import string
    li = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in li:
            li.remove(i)
    return "".join(li)
# def get_available_letters(letters_guessed):
#     import string
#     key = list(string.ascii_lowercase)
#     value = key
#     dictionary = dict(zip(key, value))
#     for i in range(len(letters_guessed)):
#         del value[i]
#         print(value)
#     return value
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split("")
    data = []
    for char in user_input:
        data.append(char)
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
