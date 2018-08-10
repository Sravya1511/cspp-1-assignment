"""comment"""
def is_valid_word(word, hand, wordList):
    if word not in wordList:
        return False
    else:
        for i in word:
            if i not in hand.keys():
                return False
    return True
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
def main():
    """string"""
    word = input()
    n = int(input())
    adict = {}
    for i in range(n):
        data = input()
        i = i+1
        i = i-1
        l = data.split()
        adict[l[0]] = int(l[1])
    l2 = input().split()
    print(is_valid_word(word,adict,l2))
if __name__ == "__main__":
    main()
