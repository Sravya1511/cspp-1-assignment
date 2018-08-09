'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''
# def get_available_letters(letters_guessed):
#     import string
#     li = list(string.ascii_lowercase)
#     for i in letters_guessed:
#         if i in li:
#             li.remove(i)
#     return "".join(li)
def get_available_letters(letters_guessed):
    """dictionary"""
    import string
    x_1 = ""
    key_ = list(string.ascii_lowercase)
    value_ = key_
    dictionary_ = dict(zip(key_, value_))
    for i in letters_guessed:
        if i in dictionary_.values():
            del dictionary_[i]
    for v_1 in dictionary_.values():
        x_1 = x_1 + v_1
    return x_1
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split(" ")
    data = []
    for char in user_input:
        data.append(char)
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
