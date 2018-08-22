def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    # print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def build_shift_dict(shift):
    dic  = {}
    import string
    a_1 = list(string.ascii_lowercase)
    b_1 = list(string.ascii_uppercase)
    c_1 = []
    d_1 = []
    for i in range(len(a_1)):
        if i < (len(a_1)-shift):
            c_1.append(a_1[i+shift])
            d_1.append(b_1[i+shift])
        else:
            for i in range(shift):
                c_1.append(a_1[i])
                d_1.append(b_1[i])
                break
    a_1.extend(b_1)
    c_1.extend(d_1)
    dic = dict(zip(a_1, c_1))
    return dic

WORDLIST_FILENAME = 'words.txt'
valid_words = load_words(WORDLIST_FILENAME)
message_text = "jgnnq"

message_text = message_text.lower().split(" ")
# message_text = message_text.split(" ")
# message_text = list(message_text)
print(message_text)
for word in message_text:
    message_text = list(word)
    print(message_text)
    for i in range(26):
        dic = build_shift_dict(i)
        m = ""
        for letter in message_text:
            for x in dic:
                if letter == dic[x]:
                    m = m+x
        if m in valid_words:
            if len(m) == len(message_text):
                print(i)
                print(m)



